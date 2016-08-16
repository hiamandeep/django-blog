from django.shortcuts import render
from django.utils import timezone
from .models import Post 
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	return render(request,'post_detail.html',{'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
	else:
		form = PostForm() 

	if form.is_valid():
    
	    post = form.save(commit=False)
	    post.author = request.user
	    post.published_date = timezone.now()
	    post.save()

	return render(request,'post_new.html',{'form':form})