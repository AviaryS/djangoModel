from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from engine.forms import PostForm
from engine.models import Post


def add_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        isPublish = request.POST.get('isPublish')
        date = request.POST.get('date')
        if isPublish:
            post = Post.objects.create(title=title, content=content, date=date)
            post.save()
            return redirect('all')
        else:
            return HttpResponse('<h2>Post not published</h2>')
    else:
        postform = PostForm()
        return render(request, 'engine/add_post.html', {'form': postform})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'engine/all_posts.html', context={'posts': posts})
