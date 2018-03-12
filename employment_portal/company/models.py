from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

from employment_portal.choices import (CITIES_CHOICES, GENDER_CHOICES,
	EDU_CHOICES)


class Employer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = PhoneNumberField(blank=False)
	name_english = models.CharField(blank=False, max_length=200)
	name_local = models.CharField(blank=False, max_length=200)
	address = models.CharField(blank=False, max_length=200)
	business_location= models.CharField(max_length= 50,
	                                    choices = CITIES_CHOICES, blank= False)
	business_license = models.ImageField(upload_to='employer/%Y/%m/%d')
	business_license_thumb = models.ImageField(upload_to='employer/%Y/%m/%d', blank=True)
	is_active = models.BooleanField(default=True)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	bio=models.CharField(blank=True, max_length=500)

	def __str__(self):
		return self.name_english

	def save(self, *args, **kwargs):
		#from employment_portal.utils import generate_thumbnail
		#self.business_license_thumb = generate_thumbnail(self.business_license)
		super(Employer, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		from employment_portal.utils import delete_from_s3
		instances_list = [self.business_license, self.business_license_thumb]
		if self.images.count() > 0:
			for image in self.images.all():
				instances_list.extend([image.image, image.thumb])
		delete_from_s3(instances_list)
		super(Employer, self).delete(*args, **kwargs)


def update_user_profile(sender, instance, created, **kwargs):
	from user_accounts.models import UserProfile
	if created:
		UserProfile.objects.filter(user=instance.user).update(user_type='Employer')


post_save.connect(update_user_profile, sender=Employer)


class EmployerRequirements(models.Model):
	employer = models.OneToOneField(Employer, on_delete=models.CASCADE)
	education = models.CharField(
			max_length=25,
			blank=True,
			choices=EDU_CHOICES,
		)
	education_major = models.CharField(max_length=50, blank=True)
	years_of_experience = models.IntegerField(blank=True)

class EmployerImages(models.Model):
	employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='images')
	cover_image = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	image = models.ImageField(upload_to='employer/%Y/%m/%d')
	thumb = models.ImageField(upload_to='employer/%Y/%m/%d', blank=True)

	def save(self, *args, **kwargs):
		from employment_portal.utils import generate_thumbnail
		self.thumb = generate_thumbnail(self.image)
		super(EmployerImages, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		from employment_portal.utils import delete_from_s3
		delete_from_s3([self.image, self.thumb])
		super(EmployerImages, self).delete(*args, **kwargs)
