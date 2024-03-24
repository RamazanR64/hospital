from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from rest_framework.routers import DefaultRouter
from .views.patient import PatientViewSet
from .views.doctor import DoctorView, ServiceViewSet, VisitViewSet

router = DefaultRouter()
router.register(r'patient', PatientViewSet, basename='patient')
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'visit', VisitViewSet, basename='visit')
router.register(r'doctor', DoctorView, basename='doctor')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('doctor/<int:doctor_id>/patient/', DoctorView.list_patient, name='doctor_patient_list'),
]
