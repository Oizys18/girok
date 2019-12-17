from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Log, Todo, TodoList, TodoListTag, TodoTag


class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Log
        fields = ('id', 'created_at', 'commited_at', 'user', 'list_rate')


class TodoListSerializer(serializers.ModelSerializer):
    todo = TodoSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ('id', 'log', 'tags', 'rate', 'todo',)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'checked', 'tags', 'todo_list',)
