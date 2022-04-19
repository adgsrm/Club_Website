from django.shortcuts import render,get_object_or_404
from .models import Member,Event,Project,Blog
# Create your views here.
def home(request):
    return render(request,"adg/index.html")

def team(request):
    team = Member.objects.all()
    return render(request,'adg/team.html', {'team' : team})

def projects(request):
    projects = Project.objects.all()
    return render(request,'adg/projects.html',{'projects':projects})

def events(request):
    events = Event.objects.all()
    return render(request,"adg/events.html",{'events':events})

def all_blogs(request):
    all_blogs = Blog.objects.all()
    return render(request,"adg/blogs.html",{'all_blogs':all_blogs})

def blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,"adg/blog-content.html",{"blog":blog})
