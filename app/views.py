from django.shortcuts import render
from .models import Post
from django.views import generic

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'index.html'
    context_object_name = 'all_posts_list'
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('?')[:10]
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['title'] = 'All Posts'
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['title'] = 'Post Detail'
        return context