from django.urls import path

from .apps import ContentConfig
from .views import *

app_name = ContentConfig.name

urlpatterns = [

    path('', ContentListApiView.as_view(), name='list_view'),
    path('create/', ContentCreateApiView.as_view(), name='create_view'),
    path('update/<int:pk>/', ContentUpdateApiView.as_view(), name='update_view'),
    path('detail/<int:pk>/', ContentRetrieveApiView.as_view(), name='detail_view'),
    path('delete/<int:pk>/', ContentDeleteApiView.as_view(), name='delete_view'),

]
