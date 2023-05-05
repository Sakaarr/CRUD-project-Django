from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import User
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    info = User.objects.all()
    return render(request, 'sakarapp/addandshow.html' , {'form':fm , 'info':info})
