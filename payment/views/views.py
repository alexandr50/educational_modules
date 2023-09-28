from django.shortcuts import render
from django.views import generic

from educational_modules.models import EducationalModule
from payment.forms import PayFormModule
from payment.models import Payment


class PayModule(generic.CreateView):
    model = Payment
    template_name = 'payment/pay_module.html'
    form_class = PayFormModule


def pay_module(request, pk):
    ed_module = EducationalModule.objects.get(pk=pk)
    form = PayFormModule()
    if request.method == 'POST':
        form = PayFormModule(data=request.POST)
    context = {'form': form}

    return render(request, 'payment/pay_module.html', context)
