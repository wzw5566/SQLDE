from rest_framework import serializers
from .models import UserRole,UserProfile,Role

class UserDetailSerializer(serializers.Serializer):
    """
    用户详情序列表类
    """
    name = serializers.CharField()
    depat_id = serializers.IntegerField()
    rolse_id = UserRole.objects.first()
    roles = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ("name", "depat_id")

    def get_roles(self, obj):
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        ret = []
        for item in roles:
            ret.append(item.role_name)
        return ret