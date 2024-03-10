from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def patch(self, request):
        profile = Profile.objects.get(user=request.user)
        #### patch 임에도 불구하고 nickname만 바꾸면 에러난다. serializer에서 3개를 필수로 받기 때문. ####  
        #### partial=True 설정해주면 에러 발생하지 않음. ####
        # serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        #### KeyError가 발생할수 있음 : data['nickname'] => data.get('nickname', profile.nickname) ####
        # profile.nickname = data['nickname']
        # profile.position = data['position']
        # profile.subjects = data['subjects']
        # if request.data['image']:
        #     profile.image = request.data['image']
        
        profile.nickname = data.get('nickname', profile.nickname)
        profile.position = data.get('position', profile.position)
        profile.subjects = data.get('subjects', profile.subjects)
        profile.image = data.get('image', profile.image)
        profile.save()
        return Response({"result": "ok"},
                        status=status.HTTP_206_PARTIAL_CONTENT)

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
