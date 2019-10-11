#### 2019년 10월 11일

# project05 - Django

> 영화데이터를 생성(Create), 조회(Read),  수정(Update), 삭제(Delete) 할 수 있는 Web Application 제작



### 1. CREATE

```python
# 영화데이터를 데이터베이스에 등록하는 기능
# GET, POST 방식에 따른 분기처리로 입력폼을 보여주거나
# 입력받은 데이터를 DB에 저장한다.
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
    
    
# 하나의 영화에 대해 상세정보 페이지에 들어가서
# 감상평을 입력받아 생성해주는 기능
def comment_create(request, m_id):
    # POST 방식
    Comment.objects.create(
        content = request.POST.get('content'),
        movie = Movie.objects.get(id=m_id),
    )
    return redirect('movies:detail', m_id)
```



### 2. READ

```python
# Main 페이지 이면서 DB에 있는 모든 영화 정보를 가져와 표시해 주는 기능
# Title 을 클릭하면 상세정보 페이지로 이동한다.
def index(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'index.html', context)


# 영화의 상세 정보를 보여주는 페이지
# 감상평을 작성, 삭제 할 수 있다.
def detail(request, id):
    context = {
        'movie': Movie.objects.get(id=id),
    }
    return render(request, 'detail.html', context)
```



### 3. UPDATE

```python
# 이미 작성된 영화정보를 DB에서 불러와 수정해 주는 기능
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
```



### 4. DELETE

```python
# 영화 정보를 삭제하는 기능
def delete(request, id):
    Movie.objects.get(id=id).delete()
    return redirect('movies:index')


# 영화 상세정보 페이지에서 감상평을 삭제하는 기능
# 영화 자체가 삭제될 경운 관련된 모든 감상평이 같이 삭제된다.
def comment_delete(request, m_id, c_id):
    Comment.objects.get(id=c_id).delete()
    return redirect('movies:detail', m_id)
```

