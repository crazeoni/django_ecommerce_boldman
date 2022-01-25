from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from boldmann_profile.forms import (EditProfileForm, ProfileForm)
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from boldmann_profile.models import UserProfile
from boldmann_profile.forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from boldmann_wears.models import Bolducts
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
@login_required
@csrf_exempt
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

		if form.is_valid() and profile_form.is_valid():
			user_form = form.save()
			custom_form = profile_form.save(False)
			custom_form.user = user_form
			custom_form.save()
			return redirect('users:login')
	else:
		profile = UserProfile.objects.get_or_create(user=request.user)
		form = EditProfileForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.userprofile)
		args = {}
		# args.update(csrf(request))
		args['form'] = form
		args['profile_form'] = profile_form
		return render(request, 'boldmann_profile/edit_profile.html', args)

@login_required
def view_profile(request):
	# jobs = Hire.objects.filter(owner=request.user).order_by('-date_posted')
	# lent = len(jobs)
	# works = Work.objects.filter(owner=request.user).order_by('-date_posted')
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

		if form.is_valid() and profile_form.is_valid():
			user_form = form.save()
			custom_form = profile_form.save(False)
			custom_form.user = user_form
			custom_form.save()
			return redirect('users:login')
	else:
		profile = UserProfile.objects.get_or_create(user=request.user)
		form = EditProfileForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.userprofile)
		args = {}
		# args.update(csrf(request))
		args['form'] = form
		args['profile_form'] = profile_form
		# args['jobs'] = jobs
		# args['works'] = works
		# args['lent'] = lent
		# return render(request, 'starrprofile/edit_profile.html', args)
		# context = {'jobs': jobs, 'works': works, 'lent': lent}
		return render(request, 'boldmann_profile/view_profile.html', args)


@csrf_exempt
@login_required	
def create_profile(request):
	if request.method != 'POST':
		form = ProfileForm()
	else:
		form = ProfileForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('boldmann_profile:view_profile'))
	context = {'form': form}
	return render(request, 'starrprofile/boldmann_profile.html', context)

# @login_required
# def profile_view(request):
	# p = User.objects.all()
	# jobs = Hire.objects.all().order_by('-date_posted')
	# email = ( user.email for user in p for job in jobs if str(user.username) == str(job.owner))
	# usernam = ( user.username for user in p for job in jobs if str(user.username) == str(job.owner))
	# imag = ( user.userprofile.image.url for user in p for job in jobs if str(user.username) == str(job.owner))
	# first_nam = ( user.userprofile.first_name for user in p for job in jobs if str(user.username) == str(job.owner))
	# last_nam = ( user.userprofile.last_name for user in p for job in jobs if str(user.username) == str(job.owner))
	# bi = ( user.userprofile.bio for user in p for job in jobs if str(user.username) == str(job.owner))
	# phone = ( user.userprofile.phoneNumber for user in p for job in jobs if str(user.username) == str(job.owner))
	# new = []
	# for i in email:
		# new.append(i)
	# t = new[0]
	# newo = []
	# for i in usernam:
		# newo.append(i)
	# t_one = newo[0]
	# newt = []
	# for i in imag:
		# newt.append(i)
	# t_two = newt[0]
	# t_ttwo = t_two[7:]
	# newtt = []
	# for i in first_nam:
		# newtt.append(i)
	# t_three = newtt[0]
	# newf = []
	# for i in last_nam:
		# newf.append(i)
	# t_four = newf[0]
	# newff = []
	# for i in bi:
		# newff.append(i)
	# t_five = newff[0]
	# news = []
	# for i in phone:
		# news.append(i)
	# t_six = news[0]
	# context = {'p': p, 't':t, 't_one':t_one, 't_ttwo':t_ttwo, 't_three':t_three, 't_four':t_four, 't_five':t_five, 't_six':t_six, 'jobs':jobs}
	# return render(request, 'starrprofile/profile_view.html',context)













from django.shortcuts import render

# Create your views here.
