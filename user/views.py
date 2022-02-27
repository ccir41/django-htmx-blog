from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .forms import SignInForm, SignUpForm


class Login(View):
    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if request.htmx:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    message = mark_safe("""<button class="toastMessage d-none" name="success">Successfully Logged In!</button>""")
                    return render(request, 'index.html', {'message': message, 'user': user})
                else:
                    form = SignInForm()
                    message = mark_safe("""<button class="toastMessage d-none" name="error">Invalid Username or Password!</button>""")
                    return render(request, 'user/login.html', {'message': message, 'form': form})
    
    def get(self, request, *args, **kwrgs):
        form = SignInForm()
        if request.htmx:
            return render(request, 'user/fragments/login.html', {'form': form})
        else:
            return render(request, 'user/login.html', {'form': form})


class Logout(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        if request.htmx:
            logout(request)
            message = mark_safe("""<button class="toastMessage d-none" name="info">You are Logged Out!</button>""")
            return render(request, 'navbar.html', {'message': message, 'user': None})


class RegisterView(FormView):
    form_class = SignUpForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('core:home')
    success_message = 'User registered successfully!'

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            template = render(request, 'index.html')
            template['Hx-Push'] = '/'
            return template

        ctx = {}
        ctx.update(csrf(request))
        form_html = render_crispy_form(form, context=ctx)
        return HttpResponse(form_html)