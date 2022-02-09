
from .models import User,UserProfile,Blog
from rest_framework import serializers
  # custom user model 



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','first_name', 'last_name', 'gender', 'zip_code')



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['email','password','user_name']
  

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length = None, use_url=True) 
    user_email = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['id','user','title','description','image','user_email']
    def get_user_email(self, blog):
        user_email = blog.user.email
        return user_email


    # # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['email'], validated_data['password'])

    #     if not username.isalnum():
    #         raise serializers.ValidationError("the username contain Alphanumeric")
    #     return attrs
