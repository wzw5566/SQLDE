# -*- coding:UTF-8 -*-
from django.db import models
#导入django自带的User模型进行扩展
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    """
    用户角色
    """
    role_name = models.CharField(max_length=100,verbose_name="角色名",help_text="角色名")

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        #使用自定义指定的表明jt_role
        db_table = "jt_role"

    def __str__(self):
        return self.role_name

class Department(models.Model):
    """
    部门
    """
    depat_name = models.CharField(max_length=64, verbose_name="部门名称", help_text="部门名称")

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        #使用自定义指定的表明jt_role
        db_table = "jt_department"

    def __str__(self):
        return self.depat_name

class UserProfile(models.Model):
    """
    在Django的User模型上进行拓展,id字段使用id
    """
    name = models.CharField(max_length=64, verbose_name="姓名")
    depat_id = models.IntegerField(verbose_name="部门id")


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        #用于指定不同的app使用不同的数据库
        # app_label = "users"
        db_table = "jt_users"

class UserRole(models.Model):
    """
    用户角色关系，为提高性能，不使用manytomany来实现
    """
    user_id = models.IntegerField(verbose_name="用户id")
    role_id = models.IntegerField(verbose_name="角色id")
    is_delete = models.BooleanField(verbose_name="是否逻辑删除", default=False)

    class Meta:
        verbose_name = "用户角色关系"
        verbose_name_plural = verbose_name
        # 使用自定义指定的表明jt_user_role
        db_table = "jt_user_role"