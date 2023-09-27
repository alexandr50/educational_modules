from django.urls import path

from .apps import CategoriesConfig
from .views.vews_api import (CategoryListApiView, CategoryRetrieveApiView,
                    CategoryCreateApiView, CategoryDeleteApiView, CategoryUpdateApiView)

app_name = CategoriesConfig.name

urlpatterns = [

    path('', CategoryListApiView.as_view(), name='list_view'),
    path('create/', CategoryCreateApiView.as_view(), name='create_view'),
    path('update/<int:pk>/', CategoryUpdateApiView.as_view(), name='update_view'),
    path('detail/<int:pk>/', CategoryRetrieveApiView.as_view(), name='detail_view'),
    path('delete/<int:pk>/', CategoryDeleteApiView.as_view(), name='delete_view'),

]
