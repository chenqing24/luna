# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from luna.quickstart.serializers import UserSerializer, GroupSerializer

'''
视图
'''
class UserViewSet(viewsets.ModelViewSet):
    '''
    查看、编辑用户界面
    常见的操作都封装在了类ViewSets
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    '''
    组界面
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer