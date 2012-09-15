from core.models import comic, publisher
from django.shortcuts import render, redirect
from django.db.models import Q

def search(request):
	context = {}
	search = request.GET.get('search', '')
	comics = comic.objects.filter(Q(name__icontains=search)\
				|Q(author__icontains=search)\
				|Q(designer__icontains=search)\
				|Q(year__icontains=search))
	context['comics'] = comics
	return render(request, 'comics.html', context)