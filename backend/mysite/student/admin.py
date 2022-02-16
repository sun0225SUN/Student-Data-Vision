# django的接口，默认已经引入。
from django.contrib import admin

# 引入我们自己写的数据表（类）
from .models import *


# 引用默认的API来自定义后台。
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'status', 'stu_id', 'name', 'sex', 'constellation', 'birthday', 'hometown', 'byword', 'created_time')
    search_fields = ('name', 'stu_id')
    # list_filter = ('sex', 'constellation', 'birthday', 'hometown', 'byword')
    list_editable = ('status',)
    fieldsets = (
        (None, {
            'fields': (
                'status',
                'stu_id',
                'name',
                'sex',
                'constellation',
                'birthday',
                'hometown',
                'byword',
            )
        }),
    )


# Register your models here.
admin.site.register(Student, StudentAdmin)
