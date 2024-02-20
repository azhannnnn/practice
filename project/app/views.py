from django.shortcuts import render
from .forms import *
from .models import *

def home(request):

    form = Adharform()
    form1 = Allotform()
    
    return render(request,'home.html',{'form':form,'form1':form1})


def add(request):
        
        adhar = request.POST['Adhar']
        data = Adhar.objects.filter(Adhar=adhar)
        form = Adharform()
        form1 = Allotform() 

        if data:
              msg="Adhar exist try different!!!!"
              return render(request,'home.html',{'form':form,'form1':form1,'msg':msg})
        else:
              Adhar.objects.create(Adhar=adhar)
              msg="Adhar added Successfully!!!!"
              return render(request,'home.html',{'form':form,'form1':form1,'msg':msg})

def allot(request):
    name = request.POST['Name']
    email = request.POST['Email']
    id = request.POST['Adhar']
    form = Adharform()
    form1 = Allotform()  

    data = Allot.objects.filter(Email=email)

    try:
        if data:
            msg="Email already alloted!!!!"
            return render(request,'home.html',{'form':form,'form1':form1,'msg1':msg})
        else:
            data1 = Adhar.objects.get(id=id)
            Allot.objects.create(Name=name,Email=email,Adhar=data1)
            msg="Adhar alloted Successfully!!!!"
            return render(request,'home.html',{'form':form,'form1':form1,'msg1':msg})

    except:
            msg="Adhar alloted to other user Please try different!!"
            return render(request,'home.html',{'form':form,'form1':form1,'msg2':msg})