
# ----------------------------------------------login--------------------------------
# from django.contrib.auth import login
# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from knox.views import LoginView as KnoxLoginView
# -------------------------------------end login-----------------------------------------
from django.shortcuts import render
from .models import UserProfile, User, Blog as Blogauth
from .serializer import RegisterSerializer, ProfileSerializer, BlogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.views import APIView # For class based view
from rest_framework import status
from rest_framework.authtoken.models import Token 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# import jwt, datetime

# Create your views here.
class Register(APIView):
# --------------------------------------------------------POST----------------------------------
    def post(self, request, format = None):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class Profile(APIView):
    authentication_classes=[JWTAuthentication]
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
# --------------------------------------------------------POST----------------------------------
    def patch(self, request, format = None):
        id = request.data.get('id')
        profile = UserProfile.objects.get(id=id)
        serializer = ProfileSerializer(profile, data = request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({'msg':'Data has been updated'})
            return Response(serializer.data)
        return Response(serializer.errors)
    # .......................................................Login....................................................
class Login(APIView):
    def post(self, request, format = None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.get(email=email)
        if user.email == email and user.password == password:
            # token = Token.objects.get_or_create(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({ 'refresh': str(refresh), 'access': str(refresh.access_token),})
            # return Response(str(token))
        return Response("user does not exist")
        #     try:
        #         token = Token.objects.get(user=user)
        #     except Token.DoesNotExist:
        #         token = Token.objects.create(user=user)
        #     return Response(token.key)def post(self, request, *args, **kwargs):

        # else:
        #     return Response([], status=status.HTTP_401_UNAUTHORIZED)
# ----------------------------Blog------------------------------------------------
class Blog(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    

   
    # ------------------------Post----------------------------------------
    def post(self, request, format = None):
        user_id = request.user.id
        print(user_id)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            request.data['user'] = user_id
            serializer = BlogSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            serializer = BlogSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)

        #  serializer = StudentSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'msg':'Data has been created'}, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST

        # -------------------------------------Get----------------------------------
    # @api_view((IsAuthenticated,))
    # @api_view((BasicAuthentication))
    def get(self, request,pk=None, format = None):
        # id = request.user.id
        # print(request.user)
        # id = request.data.get('id')
        userm = request.user.id
        if pk is not None:
            stu = Blogauth.objects.get(pk=pk, user=userm)
            serializer = BlogSerializer(stu)
            return Response(serializer.data)
        stu = Blogauth.objects.filter(user=userm)
        serializer = BlogSerializer(stu, many = True)
        return Response(serializer.data)

        #    -----------------------------------------------PUT-------------------------------------
    
    
    def put(self, request, format = None):
        id = request.data.get('id')
        user_id = request.user.id
        is_superuser = request.user.is_superuser
        if is_superuser or Blogauth.objects.filter(user_id = user_id, id = id).exists():
            # print(user_id)
            stu = Blogauth.objects.get(id = id)
            serializer = BlogSerializer(stu, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response("error not working")
# ----------------------------------------------PATCH---------------------------------------------------
    def patch(self, request, format = None):
        id = request.data.get('id')
        user_id = request.user.id
        is_superuser = user.is_superuser
        if is_superuser or Blogauth.objects.filter(user_id = user_id, id = id).exists():
            # print(user_id)
            stu = Blogauth.objects.get(id = id)
            serializer = BlogSerializer(stu, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response("error not working")
# --------------------------------------------------------------DELETE--------------------------------------
    def delete(self, request, format=None, pk=None):
        # blog_id = request.data.get('id')
        id = request.user.id # ya 
        is_superuser = request.user.is_superuser

        # if is_sueruser or (id and blog_id is not None):
        if is_superuser or Blogauth.objects.filter(user_id=id, id=pk).exists():
            stu = Blogauth.objects.get(id=pk)
            # print(stu)
            # print(stu)
            stu.delete()
            # print(stu)
            return Response({'msg':'data has been deleted'})
        return Response({'msg':'Error in delete'})

        # if is_sueruser or (id and blog_id is not None):
        #     stu = Blogauth.objects.filter(user_id=id, id=blog_id)
        #     # print(stu)
        #     # print(stu)
        #     stu.delete()
        #     # print(stu)
        #     return Response({'msg':'data has been deleted'})
        # return Response({'msg':'Error in delete'})