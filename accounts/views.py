from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import signupform, Userform, Profileform
from django.contrib.auth import authenticate, login
from .models import Profile
from home.views import getPage
from job.models import Category


# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = signupform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('accounts:profile'))
    else:
        form = signupform()
        category_obj=getPage(request,Category,4)
        cont = {'signupform': form,'cat':category_obj}
    return render(request, 'registration/signup.html', cont)


def user_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    category_obj=getPage(request,Category,4)
    return render(request, 'accounts/profile.html', {'profile': user_profile,'cat':category_obj})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = Userform(request.POST, request.FILES, instance=request.user)
        profileform = Profileform(
            request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = Userform(instance=request.user)
        profileform = Profileform(instance=profile)
        category_obj=getPage(request,Category,4)
    return render(request, 'accounts/profile_edit.html', {'profileform': profileform, 'userform': userform,'cat':category_obj})
