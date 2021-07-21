from. models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['name', 'username', 'email' , 'age' , 'phone' , 'password', 'password2']
        extra_kwargs={
            'password':{'write_only':True},
            'password2': {'write_only': True}
        }