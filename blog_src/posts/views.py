from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from posts.models import Post

# Create your views here.
from subscribers.models import Signup


def index(request):
    post_constraint = Post.objects.filter(featured_post=True)
    latest_post = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST['email']
        signup = Signup()
        signup.email = email
        signup.save()

    context = {
        'post_list': post_constraint
    }
    return render(request, 'index.html', context)


def blog(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_req_var = 'page'
    page = request.POST.get(page_req_var)
    try:
        paginated_post = paginator.page(page)
    except PageNotAnInteger:
        paginated_post = paginator.page(1)
    except EmptyPage:
        paginated_post = paginator.page(paginator.num_pages)
    context = {
        'post_list': paginated_post,
        'most_recent': most_recent,
        'page_req_var': page_req_var
    }
    return render(request, 'blog.html', context)


def post(request, id):
    return render(request, 'post.html', {})

def contacts(request):
    return render(request, 'contacts.html',)
