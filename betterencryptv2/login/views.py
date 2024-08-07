from django.shortcuts import render
from login.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')

        if User.objects.filter(username=username, credential__contains=password).exists():
            print(username + " has logged in with the password: " + password)
        
            #add to models 
            """ u = User(username=username, credential=password)
            u.save() """
            return render(request, 'dashboard/dash.html', {'username': username})
        return render(request, 'login/login.html')

    return render(request, 'login/login.html')