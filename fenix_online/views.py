from django.shortcuts import render, redirect


def about_us_page(request):
    return render(request, 'about_us.html')


def contact_page(request):
    return render(request, 'contact_us.html')