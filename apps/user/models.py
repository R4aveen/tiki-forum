from django.db import models
from django.conf import settings
import os


def user_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'users/{0}/profile.jpg'.format(instance.account)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)
        
    return profile_pic_name

def user_banner_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'users/{0}/banner.jpg'.format(instance.account)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)

    return banner_pic_name

AGE_CHOICES=(
    ('18+','18+'),
    ('Age Restricted','Age Restricted')
)

verification_options=(
    ('unverified', 'unverified'),
    ('verified', 'verified')
)

class UserAccount(models.Model):
    account = models.CharField(max_length=255, unique=True)

    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True) 
    #para saber si esta activo o no

    is_staff = models.BooleanField(default=False) 
    # para que haya un admin

    picture = models.ImageField(default='users/user_default_profile.png', upload_to=user_profile_directory_path, blank=True, null=True, verbose_name='Picture')
    banner = models.ImageField(default='users/user_default_bg.jpg', upload_to=user_banner_directory_path, blank=True, null=True, verbose_name='Banner')

    location = models.CharField(max_length=50, null=True, blank=True) #donde se ubuca
    url = models.CharField(max_length=80, null=True, blank=True) # por si el usuario porpone una url
    birthday = models.DateField(null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)

    age_limit=models.CharField(max_length=14,choices=AGE_CHOICES, null=True, blank=True) # para el limite de usuario

    verified = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name # para traer el nombre completo

    def get_short_name(self):
        return self.first_name # para traer el nombre de pila

    def __str__(self):
        return self.account # para traer el nombre de la cuenta

    def get_picture(self):
        if self.picture:
            return self.picture.url # para traer la imagen
        return ''

    def get_banner(self):
        if self.banner:
            return self.banner.url # para traer el banner
        return ''
