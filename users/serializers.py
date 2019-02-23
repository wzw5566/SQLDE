from rest_framework import serializers
from .models import UserRole,UserProfile,Role,Department

class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列表类
    """
    name = serializers.CharField()
    # depat_name = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ("name", "depat_id", "roles")

    def get_roles(self, obj):
        """
        自定义获取多对多数据
        :param obj: 当前user的实例
        :return: 角色数组
        """
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        ret = []
        for item in roles:
            ret.append(item.role_name)
        return ret

    # def get_depat_name(self,obj):
    #
    #     user = obj
    #     depat_name = Department.objects.filter(id = user.depat_id)[0].depat_name
    #     return depat_name


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    用户详情序列表类
    """
    roles = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ("name", "depat_id", "roles")

    def get_roles(self, obj):
        """
        自定义获取多对多数据
        :param obj: 当前user的实例
        :return: 角色数组
        """
        user = obj
        role_ids = UserRole.objects.filter(user_id__exact=user.id).values_list('role_id').all()
        roles = Role.objects.filter(id__in=role_ids).all()
        ret = []
        for item in roles:
            ret.append(item.role_name)
        return ret

    def create(self, validated_data):

        user = UserProfile.objects.create(** validated_data)

        try:

            role_list = self.initial_data["roles"]
            print(role_list)
            for item in role_list:

                UserRole.objects.create(user_id=user.id, role_id=item, is_delete=False)

        except Exception as e:

            print(e)

        return user


