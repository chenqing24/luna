#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from rest_framework import serializers

__author__ = 'Jeff Chen'

'''
序列化
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    User的序列化类，继承的HyperlinkedModelSerializer，用url代替唯一id
    '''
    class Meta:
        model = User # django的User模型，
        fields = ('url', 'username', 'email', 'group')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')