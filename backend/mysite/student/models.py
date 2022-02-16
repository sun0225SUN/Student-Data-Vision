from django.db import models


# Create your models here.
# 学生信息表
class Student(models.Model):
    SEX_ITEMS = [
        (0, '男'),
        (1, '女'),
    ]
    STATUS_ITEMS = [
        (0, '申请中'),
        (1, '已通过'),
        (2, '已拒绝'),
    ]
    STAR_ITEMS = [
        (0, '白羊座'),
        (1, '金牛座'),
        (2, '双子座'),
        (3, '巨蟹座'),
        (4, '狮子座'),
        (5, '处女座'),
        (6, '天秤座'),
        (7, '天蝎座'),
        (8, '射手座'),
        (9, '魔羯座'),
        (10, '水平座'),
        (11, '双鱼座'),
    ]
    stu_id = models.CharField(max_length=10, verbose_name="学号")
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="性别", default=0)
    constellation = models.IntegerField(choices=STAR_ITEMS, verbose_name="星座", default=0)
    birthday = models.DateTimeField(verbose_name="生日")
    hometown = models.CharField(max_length=128, verbose_name="家庭住址")

    byword = models.TextField(max_length=128, verbose_name="人生格言", blank=True)
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    def __str__(self):
        return '<student：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学生信息"


# 星座信息表
class StarInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="星座名字")
    value = models.IntegerField(verbose_name="数值", default=0)

    def __str__(self):
        return '<star：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "星座信息"


# 男女比例表
class SexInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="性别")
    value = models.IntegerField(verbose_name="数值", default=0)

    def __str__(self):
        return '<sex：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "男女比例"


# 省外同学地图坐标信息
class GeoInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="姓名")
    hometown = models.CharField(max_length=128, verbose_name="家乡")
    value = models.CharField(max_length=128, verbose_name="家乡坐标", default=0)
    coords = models.CharField(max_length=128, verbose_name="箭头坐标", default=0)

    def __str__(self):
        return '<name：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "省内学生"


# 省内学生信息表
class AnhuiGeoInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="姓名")
    value = models.CharField(max_length=128, verbose_name="家乡坐标", default=0)
    coords = models.CharField(max_length=128, verbose_name="箭头坐标", default=0)

    def __str__(self):
        return '<name：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "省内学生"


# 学生总数
class ProvinceInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="省份名称")
    value = models.IntegerField(verbose_name="数值", default=0)

    def __str__(self):
        return '<name：{}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学生总数"
