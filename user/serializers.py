from rest_framework.serializers import ModelSerializer

from .models import MyUser


class MyUserSerializerGET(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'email','name','img_perfil']

class MyUserSerializerPOST(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password','name','img_perfil']

    def create(self, validate_data):
        user = MyUser(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

class MyUserSerializerPUT(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username','email','password', 'name', 'img_perfil']

    def create(self, validate_data):
        user = MyUser(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    
class MyUserSerializerDELETE(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"
