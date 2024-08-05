from django.shortcuts import render, redirect


def index(request):
    return redirect('ShopHome')


def blogpost(request):
    return render(request, "blog/blogpost.html")
