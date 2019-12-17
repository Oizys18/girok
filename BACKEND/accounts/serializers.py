from rest_framework import serializers
from django.contrib.auth import get_user_model
from logs.models import Log
from logs.serializers import LogSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'is_superuser')


class UserDetailSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True)

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('logs',)
