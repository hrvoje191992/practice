from django.db import models
import uuid

# Create your models here.
class Hospital(models.Model):
	hospital_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=64)
	address = models.CharField(max_length=128)
	city = models.CharField(max_length=64)
	state = models.CharField(max_length=64)
	country = models.CharField(max_length=64)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Department(models.Model):
	department_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=32)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Doctor(models.Model):
	doctor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)
	specializations = models.CharField(max_length=64)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)

	class Meta:
		ordering = ['name']
	
	def __str__(self):
		return self.name

class Patient(models.Model):
	patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=15)
	class Meta:
		ordering = ['name']
	def __str__(self):
		self.name

class Token(models.Model):
	token_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	token_number = models.IntegerField()
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	hospital = models.ForeignKey(Hospital, on_delete=models.PROTECT)
	doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
	patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
	estimated_time = models.DateTimeField()
	# Pending | Visiting | Finished
	status = models.CharField(max_length=16)

	class Meta:
		ordering = ['hospital', 'department', 'token_number']
	
	def __str__(self):
		token_number