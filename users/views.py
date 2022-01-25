from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, get_object_or_404, reverse, Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.contrib import messages
from .forms import CustomUserCreationForm
from boldmann_profile.forms import ProfileForm
#from grindwork import helpers
#from django.core.mail import send_mail
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
UserModel = get_user_model()
#from .tokens import account_activation_token
from boldmann_profile.models import UserProfile
from boldmann_wears.models import Bolducts
from django.contrib.auth.decorators import login_required
from boldmann_profile.models import UserProfile
from django.views.generic.list import ListView

# Create your views here.
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('boldmann_wears:home'))

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
	"""Register a new user."""
	if request.method != 'POST':
		# Display blank registration form. 
		form = CustomUserCreationForm()
	else:
		# Process completed form.
		form = CustomUserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.is_active = False
			new_user = form.save()
			# Log the user in and then redirect to home page.
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return redirect('boldmann_wears:home')
			#return HttpResponseRedirect(reverse('boldmann_wears:home')
	context = {'form': form}
	return render(request, 'users/register.html', context)
