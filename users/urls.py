from users.models import BookedCalls
from users.views import RegisterView,AdvisorLists,BookedCall,Booking
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('register/',RegisterView.as_view(),name="register_user"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:id>/advisor/',AdvisorLists.as_view(),name="advisor_list"),
    path('<int:user_id>/advisor/<int:advisor_id>/',BookedCall.as_view(),name="booked_calls"),
    path('<int:user_id>/advisor/booking/',Booking.as_view(),name="booking"),



]
