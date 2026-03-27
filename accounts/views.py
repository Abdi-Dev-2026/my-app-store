from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        phone = request.POST.get('phone') 
        name = request.POST.get('name')   
        password = request.POST.get('password')
        
        if User.objects.filter(username=phone).exists():
            messages.error(request, "Lambarkan horay ayaa loo isticmaalay. Fadlan soo gal ama lambar kale isticmaal.")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=phone, password=password)
        user.first_name = name 
        user.save()
        
        messages.success(request, "Account-kaagu waa diyaar! Hadda soo gal.")
        return redirect('login')
        
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = authenticate(request, username=phone, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/') 
        else:
            messages.error(request, "Lambarka ama Password-ka waa khalad.")
            
    return render(request, 'login.html')