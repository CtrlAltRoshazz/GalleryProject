from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm , LoginForm , AddImageForm
from django.contrib.auth import authenticate , login , logout

from .models import CategoryModel , ImageModel
from django.contrib import messages

# Create your views here.

def home_view(request):
    # return HttpResponse('Home Page')

    if request.user.is_authenticated:
        return redirect('gallery')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request , user)
            messages.success(request, 'Login Successfully')
            return redirect('gallery')
        
    forms = LoginForm()
    context = {'forms':forms}
    return render(request, 'home.html', context)

def register_view(request):
    # return HttpResponse('Register Page')
    
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Register Successfully')
            return redirect('home')
        
        else:
            context = {'forms':forms}
            return render(request, 'register.html', context)

    forms = RegisterForm()
    context = {'forms' : forms}    
    return render(request, 'register.html', context)

def gallery_view(request):
    
    category = CategoryModel.objects.all()
    images = ImageModel.objects.all()
    
    context = {'category':category , 'images':images}
    return render(request, 'gallery.html', context)

def signout_view(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')
    
    
def addimage_view(request):
    forms = AddImageForm(request.POST, request.FILES)
    if forms.is_valid():
        task = forms.save(commit=False)
        task.uploaded_by = request.user
        task.save()
        messages.success(request, 'Image Added Successfully')
        
        return redirect('gallery')
    
    forms = AddImageForm()
    context = {'forms':forms}
    
    return render(request, 'addimage.html', context)


def category_view(request, id):
    category = CategoryModel.objects.all()
    images = ImageModel.objects.filter(cat = id)
    
    context = {'category':category , 'images':images}
    return render(request, 'gallery.html', context)
