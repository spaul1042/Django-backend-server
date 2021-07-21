from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework. exceptions import AuthenticationFailed
from .models import Profile
from. serializers import ProfileSerializer
import jwt, datetime


class Test(APIView):
    def get(self, request):
        profiles=Profile.objects.all()
        serializers=ProfileSerializer(profiles, many=True)
        return Response(serializers.data)


class Register(APIView):
    def post(self, request):
        password=request.data['password']
        password2 = request.data['password2']
        if password==password2:
            serializer=ProfileSerializer(data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response({"Success": "Account created successfully "})
        else:
            return Response({"Error":"Passwords do not match"})


class Login(APIView):
    def post(self, request):
         username = request.data['username']
         password = request.data['password']
         user = Profile.objects.get_by_natural_key(username=username)

         if user is None:
             return Response({"error":"User not found"})

         else:
             if user.password == password:
                 payload={
                     'id':user.id,
                     'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60), #login session will last not more than 60 minutes, means if before 60 min user refreshes cookie will disappear or otherwise cookie will itself disappear after 60 min
                     'iat':datetime.datetime.utcnow()
                 }
                 token = jwt.encode(payload,'secret', algorithm='HS256')

                 response=Response()
                 response.data={"jwt":token}
                 response.set_cookie(key='jwt', value=token , httponly=True) # httponly bcz we do not want the frontend to access token
                 return response

             else:
                return Response({"error": "Invalid Credentials"})

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token :
            raise AuthenticationFailed('Unauthenticated')
        else:
            payload = jwt.decode(token,'secret', algorithms='HS256')
            user = Profile.objects.get(id=payload['id'])
            serializer = ProfileSerializer(user, many=False)
            return Response(serializer.data)


class Update(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token :
            raise AuthenticationFailed('Unauthenticated')
        else:
            payload = jwt.decode(token,'secret', algorithms='HS256')
            user = Profile.objects.get(id=payload['id'])
            user.name=request.data['name']
            user.age = request.data['age']
            user.phone = request.data['phone']
            user.email = request.data['email']
            user.username = request.data['username']
            user.password = request.data['password']
            user.password2 = request.data['password']
            user.save()
            serializer=ProfileSerializer(user)
            return Response(serializer.data)



















