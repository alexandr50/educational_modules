from django.urls import path

from payment.apps import PaymentConfig
from payment.views.views import PayModule, pay_module

app_name = PaymentConfig.name

urlpatterns = [

    path('create/<int:pk>/', pay_module, name='pay_module'),

]
