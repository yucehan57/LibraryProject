
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

"""
1) signals form will automate creation of profile.
We will not have to go to the admin page every time
a new user needs to be created and its profile along with it.
Now, when someone registers, a default profile pic is assigned
to the user.
"""

# when a user is saved, send a signal. When received by receiver,
# it will pass it to create profile function below
@receiver(post_save, sender=User)
# create profile for each new user automatically
# will run when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.userprofile.save()
