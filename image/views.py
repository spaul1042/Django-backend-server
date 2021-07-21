from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework. exceptions import AuthenticationFailed
from .models import Profileimage
from accounts.models import Profile
from. serializers import ProfileimageSerializer
import jwt

class List(APIView):
    def get(self, request):
        images = Profileimage.objects.all()
        serializers = ProfileimageSerializer(images, many=True)
        return Response(serializers.data)

class Upload(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        else:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user = Profile.objects.get(id=payload['id'])
            image = Profileimage(
                name = request.data['name_of_image'],
                image = request.data['image']
            )
            image.uploader = user
            image.save()
            serializer = ProfileimageSerializer(image, many=False)
            return Response(serializer.data)


class Myimages(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        else:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user = Profile.objects.get(id=payload['id'])
            images = Profileimage.objects.filter(uploader=user)
            serializers = ProfileimageSerializer(images, many=True)
            return Response(serializers.data)

class Delete(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        else:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user = Profile.objects.get(id=payload['id'])
            name = request.data['name_of_image']
            image = Profileimage.objects.filter(uploader=user).filter(name=name).first()
            if image is not None:
                image.delete()
                return Response({"Deletion": "Image deleted successfully"})
            else:
                return Response({"Error": "Image does not exist"})

