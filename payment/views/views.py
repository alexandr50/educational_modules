from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from bank_card.forms import BankCardForm
from bank_card.models import BankCard
from educational_modules.forms import EdModuleForm
from educational_modules.models import EducationalModule
from payment.forms import PayFormModule
from payment.models import Payment
from users.forms import UserPayForm


class PayModule(generic.CreateView):
    template_name = 'payment/pay_module.html'
    user_form = UserPayForm
    educational_module_form = EdModuleForm
    bank_card_form = BankCardForm



    def get(self, request, *args, **kwargs):
        educational_module = EducationalModule.objects.get(pk=self.kwargs['pk'])
        my_user = self.request.user
        bank_card = BankCard.objects.filter(user=my_user).first()
        if bank_card:
            bank_card = self.bank_card_form(instance=bank_card)
        else:
            bank_card = self.bank_card_form
        context = {'ed_module': self.educational_module_form(instance=educational_module),
                   'my_user': self.user_form(instance=my_user), 'bank_card': bank_card}
        return render(request, 'payment/pay_module.html', context)

    def post(self, request, *args, **kwargs):
        educational_module = EducationalModule.objects.get(pk=self.kwargs['pk'])
        my_user = self.request.user
        context = {'ed_module': self.educational_module_form(instance=educational_module),
                   'my_user': self.user_form(instance=my_user)}
        if request.method == 'POST':
            bank_card = request.POST.get('bank_card')
            module = EducationalModule.objects.get(name=request.POST.get('name'))

            if bank_card:
                payment = Payment.objects.create(user=self.request.user,
                                                 educational_module=module,
                                                 is_done=True)
                return HttpResponseRedirect(reverse('educational_modules:list'))
            else:
                return render(request, 'payment/pay_module.html', context)

