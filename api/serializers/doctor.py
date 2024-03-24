from rest_framework import serializers
from api.models import Doctor, Service, Visit

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'specialization', 'contact_info']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class VisitSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    service = serializers.StringRelatedField()

    class Meta:

