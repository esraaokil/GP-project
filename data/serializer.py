from rest_framework import serializers
from data.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_image= serializers.ImageField(required=False)

    class Meta:
        model=Profile
        fields= '__all__'

        