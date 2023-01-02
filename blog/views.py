from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

from .models import Post



def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1) # If the page parameter is not in the GET parameters of the request, we use the default value 1 to load the first page of results    

    try:
        posts_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts_obj = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts_obj = paginator.page(paginator.num_pages)

    context = {'posts':posts_obj}

    return render(request, 'blog/post/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {
        'post': post
    }
    return render(request, 'blog/post/detail.html', context)


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'