from django.shortcuts import render,redirect
from .models import Post

# Create your views here.

def all(request):
    posts=Post.objects.all()
    return render(request,'posts/all.html',{'posts':posts})


def add(request):
    if request.method == 'POST':
        new_post = Post(
            title=request.POST['title'],
            author=request.POST['author'],
            imageUrl=request.POST['imageUrl'],
            body=request.POST['body']
        )
        new_post.save()
        return redirect('all')
    return render(request,'posts/add.html',{})



def edit(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.author = request.POST.get('author')
        post.imageUrl = request.POST.get('imageUrl')
        post.body = request.POST.get('body')
        post.save()
        return redirect('all')
    return render(request,'posts/edit.html',{"post":post})

def remove(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('all')
    return render(request,'posts/remove.html')