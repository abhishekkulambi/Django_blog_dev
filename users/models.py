from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profiles_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	#this method will run after our model is saved
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)     #super() is used to save our parent class & this is how we save parent class using super method

		#resize the profile image using PIL package
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path) 

