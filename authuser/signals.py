from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.email,
            email=user.email,
            name=user.first_name,
        )
      
        print('++++++++++++++++++++++++++++++')
        print('!!!USER CREATED')
        print('sender', sender)
        print('instance', instance)
        print(user)
        user.username = user.email
        user.save()

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    # Update name, username or email in profile, update user too.
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        print('++++++++++++++++++++++++++++++')
        print('---> USER UPDATED')
        print('sender', sender)
        print('instance', instance)



# If a profile is deleted, then delete user.
# If a user is deleted, then on_delete=models.CASCADE in model will delete profile.
def deleteUser(sender, instance, **kwargs):
    print('sender',sender)
    print('instance', instance)
    try:
        user = instance.user
        user.delete()
        print('USER DELETED')
    except:
        pass

# When user is created, a profile is created.
post_save.connect(createProfile,sender=settings.AUTH_USER_MODEL)
# If profile is updated then selected user details are updated.
post_save.connect(updateUser, sender=Profile)
# If a profile is deleted, then delete user.
post_delete.connect(deleteUser, sender=Profile)

