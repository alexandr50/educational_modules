from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import apps
from .views import *

app_name = apps.UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', UserListApiView.as_view(), name='list_view'),
    path('create/', UserCreateApiView.as_view(), name='create_view'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='update_view'),
    path('detail/<int:pk>/', UserRetrieveApiView.as_view(), name='detail_view'),
    path('delete/<int:pk>/', UserDeleteApiView.as_view(), name='detail_view'),
]
