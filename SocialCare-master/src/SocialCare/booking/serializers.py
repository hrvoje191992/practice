from .models import Hospital, Department, Doctor, Token, Patient
from rest_framework import serializers

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Hospital
		fields = [
			'hospital_id',
			'name',
			'phone',
			'email',
			'address',
			'city',
			'state',
			'country',
		]

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Department
		fields = [
			'department_id',
			'name',
		]

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Doctor
		fields = [
			'doctor_id',
			'name',
			'specializations',
			'department',
			'hospital',
		]

class PatientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Patient
		fields = [
			'patient_id',
			'name',
			'phone',
		]

class TokenSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Token
		fields = [
			'token_id',
			'token_number',
			'department',
			'hospital',
			'doctor',
			'patient',
			'estimated_time',
			'status',
		]