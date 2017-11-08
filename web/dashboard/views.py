from django.shortcuts import render
# from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.user.is_authenticated:
        print("Authenticated")
        # auth.logout(request)
    else:
        print("Not Authenticated")
    return render(request, 'dashboard.html')
