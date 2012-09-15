#encoding: utf-8

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})