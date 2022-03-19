from django.shortcuts import render

# Create your views here.
def blogHomepage(request):
    return render(request, 'blog-homepage.html')