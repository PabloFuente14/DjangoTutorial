from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """How the data should be structured in the API response"""
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serializers do not fetch data, they only transform the data into a specidied format"""
    class Meta:
        model = Group
        fields = ['url', 'name']