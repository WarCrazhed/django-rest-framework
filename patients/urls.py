from django.urls import path
from patients.views import list_patients, datail_patient

urlpatterns = [
    path('patients/', list_patients),
    path('patients/<int:pk>/', datail_patient),
]
