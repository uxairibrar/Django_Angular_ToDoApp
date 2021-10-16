from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators import csrf

from ToDoApp.models import TODO
from ToDoApp.serializers import ToDoSerializer

# Create your views here.

# TODOApi view is used for getting and posting todo records
@csrf.csrf_exempt
def TODOApi(request):
    if request.method=='GET':
        todos=TODO.objects.all()
        todos_serializer=ToDoSerializer(todos,many=True)
        return JsonResponse(todos_serializer.data, safe=False) #Safe=False means whatever we're trying to convert is in safe format
    elif request.method=='POST':
        todos_data=JSONParser().parse(request)
        todos_serializer=ToDoSerializer(data=todos_data)
        if todos_serializer.is_valid():
            todos_serializer.save()
            return JsonResponse("Record Added Successfully.",safe=False)
        return JsonResponse("Failed to Add Record.",safe=False)