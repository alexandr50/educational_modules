from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users import apps
from .views.views_api import (UserCreateApiView, UserDeleteApiView, UserUpdateApiView,
                    UserRetrieveApiView, UserListApiView)
from .views.views import RegisterUser

app_name = apps.UsersConfig.name

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', UserListApiView.as_view(), name='list_view'),
    path('create/', UserCreateApiView.as_view(), name='create_view'),
    path('update/<int:pk>/', UserUpdateApiView.as_view(), name='update_view'),
    path('detail/<int:pk>/', UserRetrieveApiView.as_view(), name='detail_view'),
    path('delete/<int:pk>/', UserDeleteApiView.as_view(), name='detail_view'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
