from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_form_view, name='employee_form'),
]
