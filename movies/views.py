from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.
def create(request):
    if request.POST:
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
            return render(request, 'list.html',{'movies' : MovieInfo.objects.all()})
    else:
        frm = MovieForm()

    return render(request, 'create.html', {'frm' : frm})


def list(request):
    movie_set = MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'list.html', {'movies' : movie_set})

def edit(request, pk):
    movie_set = MovieInfo.objects.all()
    instance_to_edit = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm = MovieForm(request.POST, instance = instance_to_edit)
        if frm.is_valid():
            instance_to_edit.save()
            return render(request, 'list.html', {'movies' : movie_set})
    frm = MovieForm(instance = instance_to_edit)
    return render(request, 'create.html', {'frm' : frm})

def delete(request, pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()

    return render(request, 'list.html', {'movies' : movie_set})
