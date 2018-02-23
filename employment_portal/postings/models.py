from django.db import models

from recruiters.models import Recruiter
from employer_admin.models import Employer
from recruit.choices import CITY_CHOICES

class City(models.Model):
	city = models.CharField(
		max_length=100
	)
	def __str__(self):
		return self.city

class Job(models.Model):
	employer - models.ForeignKey(Employer, on_delete=models.CASCADE,
	                             related_name='jobs')
	job_title = models.CharField(max_length=200)
	location=models.CharField(choices= (('onsite', 'On-site'),('remote','Remote')), max_length=50,
	                          blank=True, null=True)
	weekly_hours = models.IntegerField()
	salary_high = models.IntegerField()
	salary_low= models.IntegerField()
	Job_kind = models.CharField(choices = (('full-time', 'Full Time'),('part-time', 'Part Time')),
	                            max_length=50)
	Job_Description = models.CharField(max_length= 500)
	is_featured = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	recruiter = models.ForeignKey(Recruiter, related_name='jobs')
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	job_created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return "%d) %s: %s" % (self.pk, self.employer_admin.name_english, self.job_title)

class JobRequirements(models.Model):
	job = models.OneToOneField(Job, on_delete = models.CASCADE)
	job_skills