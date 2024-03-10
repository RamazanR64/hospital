from rest_framework import serializers
from api.models import Doctor, Service, Visit


class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    contact_info = serializers.CharField()


class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialization', 'contact_info']


class ServiceListSerializer(serializers.Serializer):
    name = serializers.CharField()


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
