from django.urls import path
from .views import TravelList, TravelDetail
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('travel-list', TravelList.as_view(), name = 'travel_list'),
    path('travel-detail/<int:pk>', TravelDetail.as_view(), name = 'travel_detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]