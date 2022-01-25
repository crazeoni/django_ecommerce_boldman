from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator, MinLengthValidator
# from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.

class UserProfileManager(models.Manager):
         pass
 
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	bio = models.TextField(null=True, validators=[MinLengthValidator(150)])
	username = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, default='', null=True)
	phoneNumber = models.CharField(
    max_length=16,
    blank=True,
    null=True,
    validators=[
      RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
      ),
    ],
  )
	image = models.ImageField(upload_to='static/profile_picture' , blank=True, null=True)
	

	def __str__(self):
		return self.user.username
	
	
	# def get_absolute_url(self):
		# return "/users/{}".format(self.slug)

def createProfile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.get_or_create(user=kwargs['instance'])

		post_save.connect(createProfile, sender=User)

