# Views provide functionality to and connect the models and templates. Common views involve the creation, listing, updating, and deleting of models.
# Views are also as simple as loading a template when visiting a certain url. 

from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Art, Profile, User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

@login_required
def home(request):
	template = loader.get_template('home.html')
	context = {}
	return HttpResponse(template.render(context, request))

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Information updated.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'profile.html', context)

@login_required
def profileEdit(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Information updated.')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'profile-edit.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# Art CRUD
class ArtListView(ListView):
	model = Art
	template = 'art.html'
	context_object_name = 'all_art'
	
	def get_queryset(self):
		return Art.objects.filter(user=self.request.user)	

class ArtDetailView(DetailView):
	model = Art

class ArtCreateView(LoginRequiredMixin, CreateView):
	model = Art
	fields = ['title', 'image', 'description', 'viewing_location', 'price', 'details']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

class ArtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Art
	fields = ['title', 'image', 'description', 'viewing_location', 'price', 'details']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		subject = self.get_object()
		if self.request.user == subject.user:
			return True
		return False

class ArtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Art
	success_url = '/gallery/'

	def test_func(self):
		subject = self.get_object()
		if self.request.user == subject.user:
			return True
		return False

# Artists

def ArtistLanding(request):
	template = loader.get_template('artist-landing.html')
	context = {}
	return HttpResponse(template.render(context, request))

class ArtistSearch(ListView):
	model = Profile
	template_name = 'artist-search.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Profile.objects.filter(
			Q(genre__icontains=query)
		)

		return object_list

class ArtistDetailView(DetailView):
	model = Profile

	def get_context_data(self, **kwargs):
		pk = kwargs.get('pk')

		context = super(ArtistDetailView, self).get_context_data(**kwargs)
		context['all_profiles'] = Profile.objects.all().values_list('id', flat=True)
		user = self.request.user
		# user_id = self.request.GET.get('current_user_id', None)
		# print(object_list)
		print(user)
		object_list = Profile.objects.filter(followers__id=user.id)
		print(object_list)
		context['object_list'] = object_list
		context['art'] = Art.objects.filter(user_id = pk)
		return context
	template_name = 'artist-review.html'


# Following
def followToggle(request, **kwargs):
	pk = kwargs.get('pk')
	currentUserObj = Profile.objects.get(id=pk)
	authorObj = Profile.objects.get(id=request.user.id)
	print(authorObj)
	print(currentUserObj)
	following = authorObj.following.all()

	print(following)

	if authorObj.id != currentUserObj.id:
		if currentUserObj in following:
			authorObj.following.remove(currentUserObj)
			print(currentUserObj)
			print('unfollow')
			print(authorObj.following.all())
		else:
			authorObj.following.add(currentUserObj)
			print(currentUserObj)
			print('follow')
			print(authorObj.following.all())
		Profile.objects.update()
	return HttpResponseRedirect(reverse(home))
	# template = loader.get_template('artist-search.html')
	# context = {}
	# return HttpResponse(template.render(context, request))

def FollowingList(request):
	template = loader.get_template('following_list.html')
	following = request.user.profile.following.all()
	print(following)
	context = {
		'all_following': following,
	}
	return HttpResponse(template.render(context, request))

class FollowingListView(ListView):
	model = Profile
	template = 'following_list.html'

	def get_queryset(self):
		user = self.request.user
		object_list = Profile.objects.filter(followers__id=user.id)
		print(user)
		print(object_list)
		return object_list

class FollowersListView(ListView):
	model = Profile
	template = 'following_list.html'

	def get_queryset(self):
		user = self.request.user
		object_list = Profile.objects.filter(following__id=user.id)
		print(user)
		print(object_list)
		return object_list

	# def get_context_data(self, **kwargs):
	# 	context = super(FollowingListView, self).get_context_data(**kwargs)
	# 	pk = kwargs.get('pk')
	# 	user = Profile.objects.get(id=self.user.id)
	# 	context['all_following'] = Profile.objects.following.all()
	# 	# context['all_following'] = Profile.objects.filter(following__isnull=False, following__id__iexact=self.kwargs.get('id'))
	# 	return context
	