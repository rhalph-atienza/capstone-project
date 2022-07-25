# urls of the "main" app of the Django project. urls are defined and connected to views here.

from . import views
from django.contrib.auth import views as auth_views
from django.urls import include, re_path, reverse_lazy

urlpatterns = [
   re_path(r'^home', views.home, name = 'home'),

   # Account Management
   re_path(r'^accounts/', include('django.contrib.auth.urls')),
   re_path(r'^accounts/logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
   re_path(r'^register', views.register, name="register"),
   re_path(r'^profile/edit', views.profileEdit, name = 'profile-edit'),
   re_path(r'^profile', views.profile, name = 'profile'),

   #Art
   re_path(r'^gallery/(?P<pk>[0-9]+)/delete', views.ArtDeleteView.as_view(), name='art-delete'),
   re_path(r'^gallery/(?P<pk>[0-9]+)/update', views.ArtUpdateView.as_view(), name='art-update'),
   re_path(r'^gallery/(?P<pk>[0-9]+)', views.ArtDetailView.as_view(), name='art-detail'),
   re_path(r'^gallery/add', views.ArtCreateView.as_view(), name='art-create'),
   re_path(r'^gallery/', views.ArtListView.as_view(), name = 'gallery'),

   #Artists
   re_path(r'^artists/(?P<pk>[0-9]+)', views.ArtistDetailView.as_view(), name='artist-detail'),
   re_path(r'^artists/search/', views.ArtistSearch.as_view(), name='artist-search'),
   re_path(r'^artists', views.ArtistLanding, name='artists'),

   #Following
   re_path(r'^followToggle/(?P<pk>[0-9]+)', views.followToggle, name='followToggle'),
   # re_path(r'^following', views.FollowingList, name='following'),
   re_path(r'^following', views.FollowingListView.as_view(), name='following'),
   re_path(r'^followers', views.FollowersListView.as_view(), name='followers'),
]
