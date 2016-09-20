from django.shortcuts import render
from django.utils import timezone
from .models import Post 
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def post_feed(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    # https://docs.djangoproject.com/en/1.9/topics/pagination/

    # contact_list = Contacts.objects.all()
    paginator = Paginator(posts, 5) # Show 5 feeds per page

    page = request.GET.get('page')
    try:
        q_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        q_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        q_set = paginator.page(paginator.num_pages)

    return render(request,'post_feed.html',{'posts':posts,'q_set':q_set}) 
    # return render(request,'post_feed.html',{'q_set':q_set}) #using q_set instead of posts due to paginator

# def post_tag_feed(request,tag):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
# 	return render(request,'tag_filter.html',{'posts':posts, 'tag':tag})

def tag_filter(request,tage):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request,'tag_filter.html',{'posts':posts,'tage':tage})


def post_detail(request,pk):
	post = Post.objects.get(pk=pk)
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #just for recent posts in the sidebar
	return render(request,'post_detail.html',{'post':post,'posts':posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_new.html', {'form': form})
