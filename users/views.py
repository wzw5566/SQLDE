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
        user = UserProfile.objects.raw('select * from jt_users')
        data = {
            "code":200,
            "msg":"success"
        }
        data['data'] = json.loads(serializers.serialize("json", user))
        return JsonResponse(data)

    def post(self, request, format=None):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 将返回结果转换成字典
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]