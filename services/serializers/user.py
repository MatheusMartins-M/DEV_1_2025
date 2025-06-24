from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="services:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email']