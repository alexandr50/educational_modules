from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from educational_modules.forms import EdModuleForm
from educational_modules.models import EducationalModule
from payment.forms import PayFormModule
from payment.models import Payment
from users.forms import UserPayForm


class PayModule(generic.CreateView):
    template_name = 'payment/pay_module.html'
    user_form = UserPayForm
    educational_module_form = EdModuleForm

    def get(self, request, *args, **kwargs):
        self.educational_module = EducationalModule.objects.get(pk=self.kwargs['pk'])
        self.user = self.request.user
        context = {'ed_module': self.educational_module_form(instance=self.educational_module),
                   'user': self.user_form(instance=self.user)}
        return render(request, 'payment/pay_module.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            bank_card = request.POST.get('bank_card')
            module = EducationalModule.objects.get(name=request.POST.get('name'))

            if bank_card:
                payment = Payment.objects.create(user=self.request.user,
                                                 educational_module=module,
                                                 is_done=True)
                return HttpResponseRedirect(reverse('educational_modules:list'))

