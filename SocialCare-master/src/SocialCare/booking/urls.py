from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hospitals', views.HospitalViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'tokens', views.TokenViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
	path('hospital/<hospital_id>', views.hospital_view, name='hospital'),
	path('track/<tracking_id>', views.tracking_view, name='track'),
	path('', views.booking_view, name='booking'),
]