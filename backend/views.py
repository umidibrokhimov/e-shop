from .models import *
from django.views.generic import TemplateView, ListView


class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'slides'

    def get_queryset(self):
        return NavSlide.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['slides'] = NavSlide.objects.all()
        context['clotheType'] = ClotheTypeCategory.objects.all()
        return context


class Shop(ListView):
    template_name = 'shop.html'
    queryset = ClotheTypeCategory.objects.all()
    context_object_name = 'clotheType'

class ProductDetail(ListView):
    template_name = 'detail.html'
    context_object_name = 'clotheType'
    queryset = ClotheTypeCategory.objects.all()