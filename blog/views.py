from django.shortcuts import render

# Create your views here.


def blog_view(request):
    from .models import Post
    
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    return render(request,'blog/blog-single.html')