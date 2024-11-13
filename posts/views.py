from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def home_page(request):
    author = request.session.get('author')
    post_list = []
    for i in Post.objects.all():
        post_list.append(i)
    post_list.reverse()

    href_prof = 'your_profile/'
    context = {
        'author': author,
        'href_prof': href_prof,
        'post_list': post_list
    }
    return render(request, 'homepage.html', context)


def authors_post(request):
    Authors = Author.objects.all()
    context = {'Authors': Authors}
    return render(request, 'authors.html', context)


def all_posts(request):
    Posts = Post.objects.all()
    context = {'Posts': Posts}
    return render(request, 'posts.html', context)


def registration(request):
    authors = Author.objects.all()
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Повтор пароля: {repeat_password}')

        if password == repeat_password:
            for i in authors:
                if str(username) == str(i.username):
                    info.update({'error': 'Пользователь уже существует'})
                    return render(request, 'registration.html', context)
            Author.objects.create(username=username, password=password)
            info.update({'info': 'Вы зарегистрированы!'})
            return redirect('/')

        else:
            if password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
            return render(request, 'registration.html', context)

    return render(request, 'registration.html', context)


def login(request):
    author_list = Author.objects.all()
    form = LoginForm()
    info = {}
    context = {
        'form': form,
        'info': info
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            for author in author_list:
                if username == author.username:
                    if password == author.password:
                        info.update({'error': 'Вход выполнен успешно!'})
                        request.session['author'] = author.username
                        return redirect('/homepage')
                info.update({'error': 'Неверный логин или пароль!'})
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)


def your_profile(request):
    author = request.session.get('author')
    author_id = Author.objects.get(username=author).id
    post_list = []
    for i in Post.objects.filter(author=author_id):
        post_list.append(i)
    post_list.reverse()

    context = {
        'author': author,
        'post_list': post_list,
    }
    if request.method == 'POST':
        if 'delete' in request.POST:
            post_id = request.POST['delete']
            Post.objects.filter(id=post_id).delete()

            post_list = []
            for i in Post.objects.filter(author=author_id):
                post_list.append(i)
            post_list.reverse()
            context['post_list'] = post_list
            return render(request, 'your_profile.html', context)

    return render(request, 'your_profile.html', context)


def create_post(request):
    creator = request.session.get('author')
    author = Author.objects.get(username=creator)
    form = CreatePost()

    info = {}
    href = '/main_page/your_profile/'
    title_command = 'Заполните форму!'
    context = {
        'form': form,
        'info': info,
        'href': href,
        'title_command': title_command,
    }
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            Post.objects.create(title=title, body=body, author=author)
            return redirect('/homepage/your_profile/')

    return render(request, 'create_post.html', context)




