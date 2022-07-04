from rest_framework import serializers
from data.models import Profile,Doctor,Patient,Review,ChestDetails,Chronic_diseases,Patient_chronic_diseases,governorates,city,Specialization


class governoratesSerializer(serializers.ModelSerializer):
    class Meta:
        model=governorates
        fields=['governorate_name_ar','governorate_name_en']

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model=city
        fields= '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Specialization
        fields= ['Specialization_name','Specialization_id']


class ProfileSerializer(serializers.ModelSerializer):
    profile_image= serializers.ImageField(required=False)

    class Meta:
        model=Profile
        #fields= ['type_name','name','email','password','gander','city_id','phone_number','profile_image']
        fields= '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['owner','doctor','review_comment','evaluation']


class DoctorSerializer(serializers.ModelSerializer):
    identification= serializers.ImageField(required=False)

    class Meta:
        model=Doctor
        fields=['type_name','name','email','password','gander','phone_number','profile_image','short_intro','bio','national_id','identification','social_website','doctor_patient_set','review','doctor_id']
        #fields= '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        #fields= '__all__'
        fields=['type_name','name','email','password','gander','phone_number','profile_image','patient_x_ray','patientDoctor','patient_id','diseases','Pregnant']

class ChestDetailsSerializer(serializers.ModelSerializer):
    x_ray_image= serializers.ImageField(required=False)

    class Meta:
        model=ChestDetails
        fields='__all__'

class Chronic_diseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chronic_diseases
        fields='__all__'


class Patient_chronic_diseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient_chronic_diseases
        fields='__all__'
