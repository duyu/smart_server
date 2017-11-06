from django.shortcuts import render
from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            print(request.session.session_key)
            auth.login(request, user)
            print(request.session.session_key)
            # Redirect to a success page.
            if user.is_superuser:
                return HttpResponseRedirect("/")
            else:
                    raise PermissionDenied
        else:
            return HttpResponseRedirect("/accounts/login/")
    else:
        return render(request, 'login.html')