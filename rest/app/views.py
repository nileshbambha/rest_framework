from django.shortcuts import render
from .models import student
from .serializers import studentserializer

from rest_framework.decorators import api_view
from rest_framework.response import Response 

@api_view(['GET'])
def studentlist(request):
    students = student.objects.all()
    serializers = studentserializer(students,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def studentdetails(request , id):
    students = student.objects.get(id=id)
    serializer = studentserializer(students,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentcreate(request):
    serializer = studentserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET'])
def studentdelete(request,id):
    students = student.objects.get(id=id)
    students.delete()    
    return Response("delete success fully")


@api_view(['POST'])
def studentupdate(request,id):
    students = student.objects.get(id=id)
    serializer = studentserializer(instance=students,data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
