from .models import *
from django.views.generic import TemplateView, ListView


class Home(ListView):
    template_name = 'index.html'
    context_object_name = 'slides'
    queryset = NavSlide.objects.all()