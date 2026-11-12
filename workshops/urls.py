from django.urls import path
from .views import register_workshop, workshop_list, workshop_success

urlpatterns = [
    path('', workshop_list, name='workshop_list'),
    path('register/<int:workshop_id>/', register_workshop, name='register_workshop'),
    path('success/<int:registration_id>/', workshop_success, name='workshop_success'),
]