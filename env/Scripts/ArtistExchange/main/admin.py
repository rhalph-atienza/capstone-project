# File that affects the Django admin page. Models are registered here in order to be viewed on the admin page.

from django.contrib import admin
from .models import Art, Profile

admin.site.register(Art)
admin.site.register(Profile)
