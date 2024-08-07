from django.shortcuts import render
from login.models import User

# Create your views here.
def gen_view(request):
    #print(User.objects.get(username="mark"))
    return render(request, 'dashboard/dash.html')