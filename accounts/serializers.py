from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'about', 'date_of_birth']
