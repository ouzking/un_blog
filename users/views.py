from django.shortcuts import render, redirect
from django.views import View
from .form import UserRegisterForm 

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'Users/register.html', {'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')