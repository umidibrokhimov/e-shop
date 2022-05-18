from django.contrib import messages
from django.shortcuts import reverse, redirect, render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .forms import *
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('e-shop:login')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user-profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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
        context['productcolors'] = ProductColor.objects.all()
        context['productsize'] = ProductSize.objects.all()
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

class ShoppingCart(ListView):
    template_name = 'cart.html'
    context_object_name = 'clotheType'
    queryset = ClotheTypeCategory.objects.all()

class Checkout(TemplateView):
    template_name = 'user-profile.html'