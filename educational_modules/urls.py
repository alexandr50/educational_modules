from django.urls import path

from .apps import EducationalModulesConfig
from .views import *

app_name = EducationalModulesConfig.name

urlpatterns = [
    path('list_ed/', EducationalModuleList.as_view(), name='list'),
    path('list_filter_ed/<int:pk>/', EducationalModuleListFilter.as_view(), name='list_filter_ed'),
    path('detail_ed_module/<int:pk>/', EducationalModuleLDetail.as_view(), name='detail_ed_module'),
    path('', EducationalModuleListApiView.as_view(), name='list_view'),
    path('create/', EducationalModuleCreateApiView.as_view(), name='create_view'),
    path('update/<int:pk>/', EducationalModuleUpdateApiView.as_view(), name='update_view'),
    path('detail/<int:pk>/', EducationalModuleRetrieveApiView.as_view(), name='detail_view'),
    path('delete/<int:pk>/', EducationalModuleDeleteApiView.as_view(), name='delete_view'),

]
