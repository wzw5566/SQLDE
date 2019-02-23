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
        """
        重载 create方法，自定义添加多表关系
        :param validated_data: 请求的验证数据
        :return: 创建成功的user序列数据
        """

        user = UserProfile.objects.create(** validated_data)

        try:

            #重点：从原始的请求数据中拿到不在model序列化中的roles数据
            role_list = self.initial_data["roles"]

            #对获得role列表数据进行循环添加
            for item in role_list:
                #为第三张关系表添加数据，user_id ,role_id
                UserRole.objects.create(user_id=user.id, role_id=item, is_delete=False)

        except Exception as e:

            print(e)

        return user


