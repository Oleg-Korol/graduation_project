from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField
from .models import UserProfile


class UserProfileSerializer(ModelSerializer):

    user = StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'