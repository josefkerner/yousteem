from django.shortcuts import render, get_object_or_404
from webapp.models import Post
from webapp.models import Category
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from steemAPI import steemAPI

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

import urllib2
import json

# Create your views here.


def index(request):

    cats = request.POST.getlist('categories[]')

    for cat in cats:
        print(cat)


    latest_post_list = steemAPI.loadPosts()
    paginator = Paginator(latest_post_list,10)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    #latest_post_list= Post.objects.filter(categories__in=cats).order_by('-score')

    #latest_post_list= Post.objects.filter(categories__in=cats).order_by('-score')
    categories = steemAPI.query('SELECT count(*) pocet, category FROM posts GROUP BY category ORDER BY pocet DESC')

    print(posts.__len__())
    #output = ', '.join([p.question for p in latest_poll_list])
    return render_to_response('webapp/index.html',{
        'posts': posts,
        'categories': categories
    })

def post_detail(request, pk):


    post = steemAPI.loadPost(pk)


    body = steemAPI().getContent(post[0]['author'],post[0]['link'])
    categories = steemAPI.query('SELECT count(*) pocet, category FROM posts GROUP BY category ORDER BY pocet DESC LIMIT 30')
    similar = steemAPI.getSimilar(post[0]['category'])
    return render_to_response('webapp/post_detail.html',{
        'post':post,
        'body': body,
        'categories': categories,
        'similar' : similar
    })

def categories(request, cat):


    query = 'SELECT * FROM posts WHERE category="'+cat+'" ORDER BY probability DESC LIMIT 30'
    posts = steemAPI.query(query)

    categories = steemAPI.query('SELECT count(*) pocet, category FROM posts GROUP BY category ORDER BY pocet DESC LIMIT 30')

    return render_to_response('webapp/category.html',{
        'posts': posts,
        'categories': categories

    })