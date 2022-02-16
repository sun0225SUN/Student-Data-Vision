from rest_framework import serializers

from .models import *  # Student, StarInfo, SexInfo, GeoInfo, AnhuiGeoInfo, ProvinceInfo


class SexInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexInfo
        fields = ['name', 'value']


# 星座信息序列化器
class StarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarInfo
        fields = ['name', 'value']


# 省外数据的序列化器

class Geo1Serializer(serializers.ModelSerializer):
    class Meta:
        model = GeoInfo
        fields = ['value']


class Geo2Serializer(serializers.ModelSerializer):
    class Meta:
        model = GeoInfo
        fields = ['coords']


# 省内数据的序列化器

class Geo3Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnhuiGeoInfo
        fields = ['value']


class Geo4Serializer(serializers.ModelSerializer):
    class Meta:
        model = AnhuiGeoInfo
        fields = ['coords']


# 省份信息序列化器
class ProvinceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceInfo
        fields = ['name', 'value']
