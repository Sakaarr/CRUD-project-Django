from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This function will add and show data
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
# this function will delete data
def delete_data(request , id):
    if request.method== 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')