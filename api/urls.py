from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

from .views.patient import PatientViewSet
from .views.doctor import DoctorView, ServiceViewSet, VisitViewSet

urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:id>',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),
    path(
        'patient/',
        PatientViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>',
        PatientViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'service/',
        ServiceViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'service/<int:id>',
        ServiceViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'visit/',
        VisitViewSet.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'visit/<int:id>',
        VisitViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
]
