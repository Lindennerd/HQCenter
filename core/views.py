from core.models import comic, publisher
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import comicForm, comentForm
from core.forms import comicForm
from django.template import RequestContext
from datetime import date
from HQCenter import settings


def home(request):
    if request.user.is_authenticated():
        user = request.user
        form = comicForm()
        if request.method =='POST':
            SaveForm = comicForm(request.POST, request.FILES)
            if SaveForm.is_valid():
                SaveForm.save()
                return redirect('core.views.home')
        context = {
            'MyComics': comic.objects.filter(exclude=False, owner_id=user.id),
            'AllComics' : comic.objects.filter(exclude=False),
            'RecentComics' : comic.objects.filter(exclude=False, post_date=date.today()),
            'form' : form
        }
    else:
        context = {
            'MyComics': [],
            'AllComics' : comic.objects.filter(exclude=False),
            'RecentComics' : comic.objects.filter(exclude=False, post_date=date.today()),
            'form' : 0
        }
    return render(request, 'index.html', context)


def update_comic(request, id):
    if not request.user.is_authenticated():
        return redirect('login_required')
    else:
        instance = get_object_or_404(comic, id=id)
        form = comicForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('core.views.home')
        return render(request, 'crud/edit_comic.html', {'form': form, 'obj_type' : 'comic'})


def delete_comic(request, id):
    if not request.user.is_authenticated():
        return redirect('login_required')
    else:
        c = get_object_or_404(comic, pk=id)
        c.exclude = True
        c.save()
        return redirect('core.views.home')


def details(request, id):
    form = comentForm()
    if request.method == 'POST':
        formComent = form(request.POST, request.FILES)
        if formComent.is_valid():
            formComent.save()
            return redirect('core.views.home')
    else:
        image = ""
        if comic.objects.filter(publisher__name="Marvel"):
            image = settings.marvel
        elif comic.objects.filter(publisher__name="DC Comics"):
            image = settings.dc_comics
        elif comic.objects.filter(publisher__name="Panini"):
            image = settings.panini
        context ={ 
            'comic' : get_object_or_404(comic, id=id),
            'image' : image,
            'form' : form
        }
    return render(request, 'details.html', context)
