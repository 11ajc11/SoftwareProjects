from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save

from employment_portal.choices import (EDU_CHOICES, Skills_choices,
                                       CITIES_CHOICES, MAJOR_CHOICES, Graduation_Choices, YEARS_OF_EXPERIENCE)


class Candidate(models.Model):
	#Personal Info
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	date_of_birth = models.DateField()

	gender = models.CharField(choices =(('male', 'Male'), ('female', 'Female'), ('other','Other'),), max_length= 10)
	nearest_metropolitan_city = models.CharField(max_length= 50,
	                                    choices = CITIES_CHOICES)
	phone_number = PhoneNumberField(blank=False)
	#Education
	education = models.CharField(max_length= 25,
	                             choices = EDU_CHOICES)
	education_major = models.CharField(max_length= 300,
	                                   choices = MAJOR_CHOICES)
	education_university = models.CharField(max_length= 45)
	years_of_experience = models.CharField(max_length=40, choices= YEARS_OF_EXPERIENCE)
	# Graduation Choices = 2018,2019,2020, 2021, Not applicable
	Graduation = models.CharField(choices=Graduation_Choices, max_length= 40, blank= True)
	bio=models.CharField(blank=True, max_length=500)
	skills_choices_1 = models.CharField(
		max_length= 25,
		choices= Skills_choices, unique= True,
        null=True
	)
	skills_choices_2 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	skills_choices_3 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	skills_choices_4 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	skills_choices_5 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	skills_choices_6 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null= True
	)
	skills_choices_7 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null = True
	)
	skills_choices_8 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null = True
	)
	skills_choices_9 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null = True
	)
	skills_choices_10 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null = True
	)
	#Candidate Image
	image = models.ImageField(upload_to= 'company/%Y/%m/%d')
	thumb = models.ImageField(upload_to= 'company/&Y/%m/%d')

	#Active or not
	is_active = models.BooleanField(default= True)
	last_modified = models.DateTimeField(auto_now_add= True, auto_now= False)
	profile_created = models.DateTimeField(auto_now= True, auto_now_add= False)

	#Saving an image
	def save(self, *args, **kwargs):
		#from employment_portal.utils import generate_thumbnail
		#self.thumb = generate_thumbnail(self.image)
		super(Candidate, self).save(*args, **kwargs)

	#Deleting an image
	def delete(self, *args, **kwargs):
		from employment_portal.utils import delete_from_s3
		delete_from_s3([self.image, self.thumb])
		super(Candidate, self).delete(*args, **kwargs)

	def __str__(self):
		return self.user.email


def update_profile_user(sender, instance, created, **kwargs):
	from user_accounts.models import UserProfile
	if created:
		UserProfile.objects.filter(user = instance.user).update(user_type = 'Candidate')


post_save.connect(update_profile_user, sender = Candidate)


class CandidateSkills(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)



class CandidateResume(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete= models.CASCADE)
	resume = models.FileField(upload_to='candidate/%Y/&m/&d')
	is_active= models.BooleanField(default=1)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	date_created = models.DateTimeField(auto_now_add=True,auto_now = False)

	def delete(self, *args, **kwargs):
		from employment_portal.utils import delete_from_s3
		delete_from_s3([self.resume])
		super(CandidateResume, self).delete(*args, **kwargs)
