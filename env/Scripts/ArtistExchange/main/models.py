# The "tables" of the Django database. Models and their fields are defined in this file.

from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_artist = models.BooleanField(default=False)
	bio = models.TextField()
	commissions_open = models.BooleanField(default=False)
	commission_rates = models.TextField()
	genre = models.TextField()
	following = models.ManyToManyField(
		"self", blank=True, related_name="followers", symmetrical=False
	)


	def __str__(self):
		return f'{self.user.username} Profile'
		
	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Art(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	image = models.ImageField(blank=True, upload_to='user_art_images')
	description = models.TextField()
	viewing_location = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	details = models.TextField() 

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('gallery')
		#return reverse('subject-detail', kwargs={'pk': self.pk})