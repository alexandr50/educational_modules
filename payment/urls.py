from django.urls import path

from payment.apps import PaymentConfig
from payment.views.views import PayModule
app_name = PaymentConfig.name

urlpatterns = [

    path('create/<int:pk>/', PayModule.as_view(), name='pay_module'),

]
