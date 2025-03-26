from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from allauth.account.utils import send_email_confirmation
from users.forms import UserForm, UserReadonlyForm
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

@login_required
def send_verification(request):
    user = request.user
    if user.is_verified:
        return redirect('profile')
    send_email_confirmation(request, user)
    print("email sent")
    return redirect('profile')

def view_profile(request, username):
    user = User.objects.get(username=username)
    if user.is_private:
        if not request.user.is_authenticated or request.user != user:
            raise Http404
    form = UserReadonlyForm(instance=user)
    context = {
        'profile_user': user,
        'form': form
    }
    return render(request, 'users/profile_view.html', context)


if settings.ENABLE_USER_SEARCH:
    def search(request):
        query = request.GET.get('q')
        if not query:
            return HttpResponse("")
        users = User.objects.filter(username__icontains=query, is_private=False)
        context = {
            'users': users
        }
        return render(request, 'users/search.html', context)