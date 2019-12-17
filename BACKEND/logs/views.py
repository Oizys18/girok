from django.shortcuts import render, get_object_or_404
from .models import Log, Todo, TodoList, TodoListTag, TodoTag
from .serializers import LogSerializer, TodoSerializer, TodoListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def logs(request):
    logs_all = Log.objects.all()
    serializer = LogSerializer(logs_all, many=True)
    return Response(serializer.data)


# @api_view(['GET', 'POST', 'DELETE'])
# def 