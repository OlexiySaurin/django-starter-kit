from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from users.forms import UserForm
from users.models import User


def index(request):
    return render(request, 'index.html')

@login_required
def profile_page(request):
    form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'account/profile.html', context)

@require_http_methods(['POST'])
def check_username(request):
    username = request.POST.get('username')
    if not username:
        return HttpResponse("")
    if User.objects.filter(username=username).exists():
        return HttpResponse('<span class="text-danger">Username already exists</span>')
    return HttpResponse('<span class="text-success">Username is available</span>')

@require_http_methods(['POST'])
def check_password(request):
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if password1 == password2:
        return HttpResponse('')
    return HttpResponse('<span class="text-danger">Passwords not match</span>')