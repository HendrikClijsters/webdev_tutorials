from django.shortcuts import render

# Create your views here.
def home(request):
    title = "This is my title."
    context = {'title':title}
    return render(request, 'posts/home.html', context)

def blogposts(request):
    context = {}
    return render(request, 'posts/blogposts.html', context)
