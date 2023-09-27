from django.shortcuts import get_object_or_404
from django.views import generic

from categories.models import Category
from content.models import Content
from payment.forms import PyaFormModule
from educational_modules.models import EducationalModule


class EducationalModuleList(generic.ListView):
    model = EducationalModule
    template_name = 'educational_modules/list_educational_modules.html'
    extra_context = {
        'title': 'Список модулей'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return EducationalModule.objects.all()



class EducationalModuleListFilter(generic.ListView):
    model = EducationalModule
    template_name = 'educational_modules/list_educational_modules.html'
    extra_context = {
        'title': 'Список модулей'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context

    def get_queryset(self, id_category=None):
        id_category = self.kwargs['pk']
        qs = EducationalModule.objects.filter(category_id=id_category)
        return qs


class EducationalModuleLDetail(generic.DetailView):
    model = EducationalModule
    template_name = 'educational_modules/educational_module.html'
    extra_context = {
        'title': 'Информация о модуле'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educational_module'] = get_object_or_404(EducationalModule, pk=self.kwargs['pk'])
        context['content'] = Content.objects.filter(educational_module__pk=context['educational_module'].pk)
        return context


class PayModule(generic.UpdateView):
    model = EducationalModule
    template_name = 'educational_modules/pay_module.html'
    form_class = PyaFormModule


