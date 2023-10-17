from rest_framework.serializers import ModelSerializer

from user.models import MyUser


class MyUserSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"

    def create(self, validate_data):
        user = MyUser(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user