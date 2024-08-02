from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def hello_world_string(request):
    return HttpResponse('<h1>Hello World from String!</h1>')

def hello_world_html(request):
    return render(request, 'hello_world.html')

def hello_world_jinja(request):
    motor = 'Jinja'
    return render(request, 'hello_world_jinja.html', {
        'motor': motor
    })

def hello_world_form(request):
    print(request.POST)
    if request.method == 'GET':
        print('sending_form')
        return render(request, 'hello_world_form.html', {
        'form': UserCreationForm
    })
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return render(request, 'hello_world_form.html', {
                    'form': UserCreationForm,
                    'message': 'User created successfully'
                })
            except Exception as e:
                print(e)
                return render(request, 'hello_world_form.html', {
                    'form': UserCreationForm,
                    'message': 'Username already exists'
                })
        return render(request, 'hello_world_form.html', {
            'form': UserCreationForm,
            'message': 'Password do not match'
        })
    return render(request, 'hello_world_form.html', {
        'form': UserCreationForm
    })