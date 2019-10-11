from django.shortcuts import render, redirect
from .models import Movie, Comment

# Create your views here.
def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        movie = Movie.objects.create(
            title = request.POST.get('title'),
            title_en = request.POST.get('title-en'),
            audience = request.POST.get('audience'),
            open_date = request.POST.get('open-date'),
            genre = request.POST.get('genre'),
            watch_grade = request.POST.get('watch-grade'),
            score = request.POST.get('score'),
            poster_url = request.POST.get('poster-url'),
            description = request.POST.get('description')
        )
        return redirect('movies:index')
    else:
        return render(request, 'form.html')


def detail(request, id):
    context = {
        'movie': Movie.objects.get(id=id),
    }
    return render(request, 'detail.html', context)


def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.title_en = request.POST.get('title-en')
        movie.audience = request.POST.get('audience')
        movie.open_date = request.POST.get('open-date')
        movie.genre = request.POST.get('genre')
        movie.watch_grade = request.POST.get('watch-grade')
        movie.score = request.POST.get('score')
        movie.poster_url = request.POST.get('poster-url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', id)
    else:
        context = {
            'movie': movie,
        }
        return render(request, 'form.html', context)


def delete(request, id):
    Movie.objects.get(id=id).delete()
    return redirect('movies:index')


def comment_create(request, m_id):
    # POST 방식
    Comment.objects.create(
        content = request.POST.get('content'),
        movie = Movie.objects.get(id=m_id),
    )
    return redirect('movies:detail', m_id)

def comment_delete(request, m_id, c_id):
    Comment.objects.get(id=c_id).delete()
    return redirect('movies:detail', m_id)