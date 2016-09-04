from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from forms import RegistrationForm

def registration_complete(request):
     return render_to_response('accounts/registration_complete.html')

def loggedin(request):
    return render_to_response('registration/loggedin.html',{'username': request.user.username})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')