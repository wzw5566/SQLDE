from rest_framework import serializers
from .models import *

class UserDetailSerializer(serializers.Serializer):
    """
    用户详情序列表类
    """
    name = serializers.CharField()
    depat_id = serializers.IntegerField()
    rolse_id = UserRole.objects.first()
    # roles = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ("name", "depat_id")

    # def get_roles(self, obj):
    #
    #     role_object_list = obj.roles.all()
    #     ret = []
    #     for item in role_object_list:
    #         ret.append({item.role_name})
    #     return ret