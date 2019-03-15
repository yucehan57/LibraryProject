from django.db import models
from django.contrib import auth

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        #built in username attribute of the User model
        return "{}".format(self.username)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
