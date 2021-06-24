from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def form1(request):
    if request.method=="POST":
        #print(request.POST)
        print(request.POST.get("name"))
        print(request.POST.get("emailid"))
        print(request.POST.get("phno"))
        print(request.POST.get("gender"))
    return render(request,"form1.html")

def form2(request):
    if request.method=="POST":
        #print(request.POST)
        print(request.POST.getlist("hobby"))
        print(request.POST.getlist("fav"))
        
    return render(request,"form2.html")