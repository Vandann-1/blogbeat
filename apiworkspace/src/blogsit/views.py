from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import stblog


# Create your views here.


class createblog(CreateAPIView0):
    queryset = stblog.objects.all()
    serializer_class=stblogSerializer
