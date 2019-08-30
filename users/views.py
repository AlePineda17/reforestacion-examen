from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from .models import User


def register_user(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            password=request.POST['password'],
            is_admin='is_admin' in request.POST and request.POST['is_admin'],
        )
        new_user.save()
        return HttpResponseRedirect(reverse('users:login'))

    elif request.method == 'GET':
        template = 'users/register_user_form.html'
        return render(request, template)
    return HttpResponse('Error: method not allowed.')


def login_user(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST['email'], password=request.POST['password'])
        except user.DoesNotExist:
            return HttpResponse('User does not exist.')
        return HttpResponseRedirect(reverse('fincas:index', kwargs={'user_id':user.pk}))

    elif request.method == 'GET':
        template = 'users/login_user_form.html'
        return render(request, template)
    return HttpResponse('Error: method not allowed.')

