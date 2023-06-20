from django.urls import path
from .views import CreateListAccountView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('accounts/', CreateListAccountView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]