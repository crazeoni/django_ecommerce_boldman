from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from boldmann_profile.models import UserProfile

class EditProfileForm(ModelForm):
	class Meta:
		model = User
		fields = (
					'email',
                )
class ProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'bio', 'city', 'phoneNumber', 'image',) 
		#Note that we didn't mention user field here.

