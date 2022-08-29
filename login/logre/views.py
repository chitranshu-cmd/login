from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def home(request):

    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        age = request.POST['age']

        user =User.object.create_user()
        user.save()
        print('user created')
        return redirect('/')

    return render(request,"home.html")




# Create your views here.
