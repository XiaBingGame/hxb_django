from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.http import HttpResponse


def home(request):
    post_list = Post.published.all()
    return render(request, 'blog/post/home.html', {'post_list': post_list})

def detail(request, id):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             # publish__month=month,
                             # publish__day=day
                             )
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   #publish__month=month,
                                   #publish__day=day
                             )
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})


def post_test(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published')
    #return render(request, 'blog/post/detail.html', {'post':post})
    str_t = post.publish.month
    return HttpResponse(str_t)
