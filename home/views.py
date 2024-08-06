from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Upload
from .forms import UploadForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LoginView(AuthLoginView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm



@login_required
def home(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('output')
        else:
            form = UploadForm()
    context = {'form': form}
    return render(request, 'index.html', context)

@login_required
def output(request):
    img = Upload.objects.last()
    context = {'img': img}
    return render(request, 'output.html', context)