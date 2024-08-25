from rest_framework import serializers
from users.models import User
from users.validators import UserValidator


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        validators = [UserValidator(field='password')]
