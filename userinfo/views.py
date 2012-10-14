from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from userinfo.forms import UserForm, PasswordReset
#mudança

def settings(request):
    user = request.user
    instance = get_object_or_404(User, id=user.id)
    form = UserForm(request.POST or None, instance=instance)
    cngpwd = PasswordReset(user = request.user, data = request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core.views.home')
    if cngpwd.is_valid(): 
        print cngpwd.clean_password2()
        user.set_password(cngpwd.clean_password2())
        user.save()
    return render(request, 'user_settings.html', {'form': form, 'cngpwd' : cngpwd })

def change_password(request):
    print 0
    user = request.user
    u = get_object_or_404(User, id=user.id)
    if request.POST:
        u.set_password(request.POST["password"])
    return redirect('core.views.home')
