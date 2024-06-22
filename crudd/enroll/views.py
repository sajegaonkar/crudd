from django.shortcuts import render

from enroll.forms import EmployeeRegistration

from .models import UserProfile

from django.http import HttpResponseRedirect

# Create your views here.

def test(request):
    if request.method == 'POST':
        print(request,"request")
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = EmployeeRegistration()
    else:
        fm = EmployeeRegistration()

    userData = UserProfile.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'userData':userData})

def delete(request,id):
    if request.method == 'POST':
        pi = UserProfile.objects.get(pk=id)
        pi.delete()
    
    return HttpResponseRedirect('/enroll')

def updatedata(request,id):
    if request.method=='POST':
        pi=UserProfile.objects.get(pk=id)
        fm=EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=UserProfile.objects.get(pk=id)
        fm=EmployeeRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
    


