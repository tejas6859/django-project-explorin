from rest_framework import serializers
from webapp.models import blog,User,Tag

class blogSerializer(serializers.ModelSerializer):

    class Meta:
        model = blog
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'        