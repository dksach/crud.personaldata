from django.shortcuts import render,redirect
from . models import User

def index(request):
    data={
        
        'usersData':User.objects.all()
    }
    return render(request,'index.html',data)

def insert(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        image = request.POST.get('image')
        language =request.POST.get('language')
        User.objects.create(name=name,email=email,gender=gender,country=country,image=image,language=language)
        return redirect('/')
    else:
        return redirect('/')
    
def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect('/') 

def edit(request,id):
    if request.method == 'POST':
        sobj=User.objects.get(id=id)
        sobj.name = request.POST.get('name')
        sobj.email = request.POST.get('email')
        sobj.gender = request.POST.get('gender')
        sobj.language = request.POST.get('language')
        sobj.country = request.POST.get('country')
        sobj.image = request.POST.get('image')
        sobj.save()
        return redirect('/')
    else:
        data={
            'usersData':User.objects.get(id=id)
        }
        return render(request,'edit.html',data)

