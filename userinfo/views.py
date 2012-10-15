from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from userinfo.forms import UserForm, PasswordReset, UserPicForm
from django.forms.formsets import formset_factory

def settings(request):
    user = request.user
    instance = get_object_or_404(User, id=user.id)
    form = UserForm(request.POST or None, instance=instance)
    form_pwd = PasswordReset(user = request.user, data = request.POST or None)
    UserPic = UserPicForm(request.POST)
    if form.is_valid():
        form.save()
    if form_pwd.is_valid():
        user.set_password(form_pwd.clean_password2())
        user.save()
    if UserPic.is_valid():
        user.profile_image = UserPic.cleaned_data.get('userpic')
        user.save()
    return render(request, 'user_settings.html', {'form': form, 'form_pwd': form_pwd, 'userpic': UserPic})