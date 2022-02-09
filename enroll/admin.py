from django.contrib import admin
from .models import User,UserProfile,Blog


# admin.site.register(UserProfile)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email','password']

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','first_name','last_name','gender','zip_code']

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['id', 'user','title','description','image']




