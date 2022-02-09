
# from .managers import CustomUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import MinLengthValidator
from django.db.models.signals import pre_init, pre_save, pre_delete, post_delete, post_save, post_init


class User(AbstractUser):
    username = None
    
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    user_name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.email

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance= None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user = instance)

class UserProfile(models.Model):
    GENDER = (
    ('M', 'Homme'),
    ('F', 'Femme'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], blank=False)
    



def create_profile(sender, instance, created, **kwargs):
    # print(instance.user_name) mean ak row
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)


class Blog(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    description = models.CharField(max_length = 255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/', max_length =255, null= True, blank=True)

      