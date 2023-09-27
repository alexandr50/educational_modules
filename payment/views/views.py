from django.views import generic

from payment.forms import PyaFormModule


class PayModule(generic.UpdateView):
    model = Payment
    template_name = 'educational_modules/pay_module.html'
    form_class = PyaFormModule
