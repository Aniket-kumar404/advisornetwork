from users.views import RegisterView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import AdvisorView

urlpatterns = [
path('advisor/',AdvisorView.as_view()),
]
