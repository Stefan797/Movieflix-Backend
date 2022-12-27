from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import CustomUser
from django.core import serializers
from django.http import HttpResponse
from .serializers import CustomUserSerializer
# Create your views here.







class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-id')
    serializer_class = CustomUserSerializer

#    def create(self, request):
#       if request.method == 'POST':
#            """
#            This is a view to create an CustomUser.
#            """
#            new_User = CustomUser.objects.create(
#                email=request.POST['email'], 
#                first_name=request.POST['first_name'], 
#                last_name=request.POST['last_name'],
#                password=request.POST['password'])
#            new_User.save()

           # serzialized_customUser = serializers.serialize('json', [new_User, ])
         #   return HttpResponse(serzialized_customUser, content_type='application/json')


# date_joined mit aktuellem datum versehen


# https://stackoverflow.com/questions/58811689/django-username-is-empty-when-a-new-user-is-created-when-signing-in

""" def login_user(request):
logout(request)
if request.POST:
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/mainpage/')
    else:
        login_message = "Your username or password is incorrect."
        return render(request, 'index.html', {'login_message': login_message})
return render(request, 'index.html')

def sign_up(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']
        if(valid_form(username, email, password, password_confirm)):
            #create the new user
            user = CustomUser(name=username, email=email, password=password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/mainpage/')
        else:
            message = "There was a problem."
            return render(request, 'index.html', {'message': message})
    return render(request, 'index.html') """