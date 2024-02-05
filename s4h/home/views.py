from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def learn(request):
    return render(request,"home/learn.html")

def contribute_index(request):
    return render(request, "home/contributor_index.html")
def contribute(request,contributor):
    return render(request,"home/contribute.html", {
        "contributor": contributor.capitalize()
    })

def social_media(request):
    return render(request,"home/social_media.html")

def stories(request):
    return render(request,"home/stories.html")

def events(request):
    return render(request,"home/events.html")