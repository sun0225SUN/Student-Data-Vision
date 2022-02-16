from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.viewsets import ModelViewSet

from .forms import StudentForm
from .models import *  # Student, StarInfo, SexInfo, GeoInfo, AnhuiGeo

from .serializers import *  # StarInfoSerializer, SexInfoSerializer, Geo1Serializer, Geo2Serializer, Geo3Serializer, \
# Geo4Serializer  # StudentSerializer,

import requests, json


# Create your views here.
# 用户提交信息数据
def info(request):
    # 如果请求方法是POST
    if request.method == 'POST':
        # form存储提交的所有数据
        form = StudentForm(request.POST)
        # 如果提交的全部正确
        if form.is_valid():
            # 储存数据
            form.save()
            # 跳转到成功页面
            return HttpResponseRedirect(reverse('student:succeed'))
    else:
        # 如果数据不符合要求（填写不符合规范）空表单
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'info.html', context=context)


# 提交数据成功
def succeed(request):
    # 获取student表里的所有对象
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'succeed.html', context=context)


# 此类用于计算和更新数据
class data_compute():

    # 更新星座数据
    def star_update(self):
        star_list = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
        queryset = Student.objects.all()
        # 遍历十二个整形数据，其在数据库中对应的是十二个星座
        for star_number in range(12):
            # 开始遍历star_number个星座
            # 计数
            count_value = 0
            # 遍历所有对象，统计当前星座的个数
            for item in queryset:
                if item.constellation == star_number:
                    count_value += 1
            # 如果StarInfo表中该星座行已经创建，说明该星座value变了，需要更新(修改)value数据
            if StarInfo.objects.filter(name=star_list[star_number]).exists():
                instance = StarInfo.objects.get(name=star_list[star_number])
                # print(count_value)
                instance.value = count_value
                instance.save()
            # 如果StarInfo表中该星座行没有创建，那么我们创建该表
            else:
                StarInfo.objects.create(name=star_list[star_number], value=count_value)
        print("星座数据已经更新完毕！")
        return None

    # 更新性别数据
    def sex_update(self):
        sex_list = ['男', '女']
        queryset = Student.objects.all()
        for sex_number in range(2):
            count_value = 0
            for item in queryset:
                if item.sex == sex_number:
                    count_value += 1
            # 如果StarInfo表中该星座行已经创建，说明该星座value变了，需要更新(修改)value数据
            if SexInfo.objects.filter(name=sex_list[sex_number]).exists():
                instance = SexInfo.objects.get(name=sex_list[sex_number])
                instance.value = count_value
                instance.save()
            else:
                SexInfo.objects.create(name=sex_list[sex_number], value=count_value)
        print("性别数据已经更新完毕！")
        return None

    # 更新地理数据
    def geo_update(self):
        queryset = Student.objects.all()
        for item in queryset:
            address = ''
            address = item.hometown
            url = 'https://restapi.amap.com/v3/geocode/geo?address=' + str(address)
            params = {
                'key': '2fa9633ba7fee11266e2812b7e89595d'
            }
            response = requests.get(url=url, params=params)
            r = response.json()
            location_data = '[' + r["geocodes"][0]['location'] + ']'
            location = eval(location_data)
            coords_list = []
            aust = [117.011140, 32.641538]
            coords_list.append(location)
            coords_list.append(aust)
            # 判断是省外的同学
            # if item.hometown[:2]!='安徽'
            if item.hometown[:3] != '安徽省':
                # 如果实例存在则更新数据
                if GeoInfo.objects.filter(name=item.name).exists():
                    instance = GeoInfo.objects.get(name=item.name)
                    instance.value = location
                    instance.hometown = item.hometown
                    instance.coords = coords_list
                    instance.save()
                # 不存在则新建行，存储该数据。
                else:
                    GeoInfo.objects.create(name=item.name, value=location, coords=coords_list)
            else:
                if AnhuiGeoInfo.objects.filter(name=item.name).exists():
                    instance = AnhuiGeoInfo.objects.get(name=item.name)
                    instance.value = location
                    instance.coords = coords_list
                    instance.save()
                # 不存在则新建行，存储该数据。
                else:
                    AnhuiGeoInfo.objects.create(name=item.name, value=location, coords=coords_list)
        print("地理数据已经更新完毕！")
        return None

    # 更新星座数据
    def province_update(self):
        # 查询学生的信息
        queryset = Student.objects.all()

        # 定义存储全国省份的列表
        province_list_2 = ['河北', '山西', '辽宁', '吉林', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南',
                           '四川', '贵州', '云南', '陕西', '甘肃', '青海', '台湾', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆',
                           '香港', '澳门']
        province_list_3 = ['黑龙江', '内蒙古']

        # 遍历两个字的省份
        for province_item in province_list_2:
            # 初始化此省份学生个数为0
            count_value = 0
            # 遍历学生数据
            for stu_item in queryset:
                # 如果改省份的名字等于学生家乡的前两个字，则记录改值
                if province_item == stu_item.hometown[0:2]:
                    # 该省份学生数 +1
                    count_value += 1
                    # 如果此省份信息已经在数据表中记录，则更新当前数据
                    if ProvinceInfo.objects.filter(name=stu_item.hometown[0:2]).exists():
                        instance = ProvinceInfo.objects.get(name=stu_item.hometown[0:2])
                        # print(count_value)
                        instance.value = count_value
                        instance.save()
                    # 如果此省份信息没有在数据表中记录，则创建该表
                    else:
                        ProvinceInfo.objects.create(name=stu_item.hometown[0:2], value=count_value)

        # 同理 遍历三个字的所有省份数据，将列表和切片更改写就好了
        for province_item in province_list_3:
            # 初始化此省份学生个数为0
            count_value = 0
            # 遍历学生数据
            for stu_item in queryset:
                # 如果改省份的名字等于学生家乡的前两个字，则记录改值
                if province_item == stu_item.hometown[0:3]:
                    # 该省份学生数 +1
                    count_value += 1
                    # 如果此省份信息已经在数据表中记录，则更新当前数据
                    if ProvinceInfo.objects.filter(name=stu_item.hometown[0:3]).exists():
                        instance = ProvinceInfo.objects.get(name=stu_item.hometown[0:3])
                        # print(count_value)
                        instance.value = count_value
                        instance.save()
                    # 如果此省份信息没有在数据表中记录，则创建该表
                    else:
                        ProvinceInfo.objects.create(name=stu_item.hometown[0:3], value=count_value)
        print("省份数据已经更新完毕！")
        return None


# 此方法用作更新数据，当学生信息表中的数据有变化时，更新相应的数据分析的数据。
def update(request):
    data_instance = data_compute()
    data_instance.star_update()
    data_instance.sex_update()
    data_instance.geo_update()
    data_instance.province_update()
    return HttpResponse('<h1 align="center">数据更新成功！</h1>')


# 星座信息序列化器
class StarInfoViewSet(ModelViewSet):
    queryset = StarInfo.objects.all()
    serializer_class = StarInfoSerializer


class SexInfoViewSet(ModelViewSet):
    queryset = SexInfo.objects.all()
    serializer_class = SexInfoSerializer


class Geo1ViewSet(ModelViewSet):
    queryset = GeoInfo.objects.all()
    serializer_class = Geo1Serializer


class Geo2ViewSet(ModelViewSet):
    queryset = GeoInfo.objects.all()
    serializer_class = Geo2Serializer


class Geo3ViewSet(ModelViewSet):
    queryset = AnhuiGeoInfo.objects.all()
    serializer_class = Geo3Serializer


class Geo4ViewSet(ModelViewSet):
    queryset = AnhuiGeoInfo.objects.all()
    serializer_class = Geo4Serializer


class ProvinceInfoViewSet(ModelViewSet):
    queryset = ProvinceInfo.objects.all()
    serializer_class = ProvinceInfoSerializer
