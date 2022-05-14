from .models import *
from django.views.generic import TemplateView, ListView, DetailView


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
    context_object_name = 'clotheType'

    def get_queryset(self):
        return ClotheTypeCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Shop, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['clotheType'] = ClotheTypeCategory.objects.all()
        context['products'] = Products.objects.all()
        return context

class ProductDetail(DetailView):
    template_name = 'detail.html'
    queryset = Products.objects.all()
    context_object_name = 'product'

    def get_queryset(self):
        return Products.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        # here we can add so many context using that way
        context['clotheType'] = ClotheTypeCategory.objects.all()
        context['products'] = Products.objects.all()
        return context

class Contact(ListView):
    template_name = 'contact.html'
    context_object_name = 'clotheType'
    queryset = ClotheTypeCategory.objects.all()