from django.shortcuts import render,HttpResponse
from mi.models import Submit

# Create your views here.
def contact(request):
    return render(request,'contact.html')
def sign(request):
    return render(request,'signin.html')    
def make(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')    
def submit(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        submit=Submit(username=username,password=password,phone=phone,email=email)
        submit.save()
        return render(request,'thanks.html')   
    return render(request,'index.html')    