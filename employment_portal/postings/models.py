from django.db import models

from recruiters.models import Recruiter
from company.models import Employer
from employment_portal.choices import (CITIES_CHOICES, Skills_choices)

class City(models.Model):
	city = models.CharField(
		max_length=100
	)
	def __str__(self):
		return self.city

class Job(models.Model):
	Employer_Name = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs')
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
	recruiter = models.ForeignKey(Recruiter, related_name='jobs', on_delete=models.CASCADE)
	last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
	job_created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return "%d) %s: %s" % (self.pk, self.employer_admin.name_english, self.job_title)

class JobRequirements(models.Model):
	job = models.OneToOneField(Job, on_delete = models.CASCADE)
	job_skills_1 = models.CharField(
		max_length= 25,
		choices= Skills_choices, unique= True
	)
	job_skills_2 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_3 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_4 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_5 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_6 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_7 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_8 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_9 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)
	job_skills_10 = models.CharField(
		max_length=25,
		choices=Skills_choices, unique=True,
		null=True
	)

