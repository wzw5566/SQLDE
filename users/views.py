from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from rest_framework import serializers

from users.models import *
from users.serializers import UserDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse,JsonResponse
import json
from django.core import serializers

class UserListView(APIView):
    def get(self, request, format=None):
        # user = UserProfile.objects.all()
        user = UserProfile.objects.raw('select * from jt_users')

        # data = dictfetchall(user)

        data = json.loads(serializers.serialize("json", user))
        data_result = {
            "code":200,
            "msg":"success" ,
            "data":data
        }

        return JsonResponse(data_result)


    def post(self, request, format=None):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersView(APIView):
    """
    序列化方式获得多对多
    """
    def get(self, request, format=None):
        user = UserProfile.objects.all()
        user_serializer = UserDetailSerializer(user, many=True)
        return JsonResponse(user_serializer.data,safe=False)
