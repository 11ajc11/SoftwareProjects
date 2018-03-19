from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from company.models import Employer


class Recruiter(models.Model):
	Employer_Name = models.ForeignKey(Employer, on_delete=models.CASCADE,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = PhoneNumberField()
	date_of_birth = models.DateField()
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to='recruiter/%Y/%m/%d', null=True)
	thumb = models.ImageField(upload_to='recruiter/%Y/%m/%d', blank=True, null=True)
	is_active = models.BooleanField(default=True)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	def __str__(self):
		return self.user.__str__()



def update_user_profile(sender, instance, created, **kwargs):
	from user_accounts.models import UserProfile
	if created:
		UserProfile.objects.filter(user=instance.user).update(user_type='Recruiter')


post_save.connect(update_user_profile, sender=Recruiter)
