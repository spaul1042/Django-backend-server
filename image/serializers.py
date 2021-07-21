from rest_framework import serializers
from .models import Profileimage


class ProfileimageSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profileimage
        fields = ['image', 'uploader', 'name']