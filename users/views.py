from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .MyPage import MyPageNumberPagination
class UsersViewTest(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        print(request.data)
        return self.create(request)


class UserView(ListAPIView):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
   pagination_class = MyPageNumberPagination # 配置自定义的分页启


class UsersDetailView(APIView):

    def delete(self,request,pk):
        Users.objects.filter(id=pk).delete()
        return Response("删除成功!")
class LoginView(APIView):

    def get(self,request):

        return Response({'message':'请使用POST请求登录!'})

    def post(self,request):
        serializer = UsersSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        uname = request.data['username']
        pwd = request.data['password']
        if Users.objects.filter(username=uname):
            user = Users.objects.filter(username=uname,password=pwd)
            if user:
                return Response({'message':'登录成功!'})
            else:
                return Response({'message':'密码错误，请重新输入密码!'})
        else:
            return Response({'message':'用户名不存在,请注册!'})


class RegisterView(APIView):

    def post(self,request):
        serializer = UsersSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        uname = request.data.get('username')
        print(uname)
        user = Users.objects.filter(username=uname)
        if Users.objects.filter(username=uname):
            return Response({'message':'用户名已存在!'})
        Users.objects.create(**serializer.data)
        return Response({'message':'注册成功!'})