from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Post
from .forms import PostForm



class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html' #생략가능
    context_object_name = 'posts' #생략가능
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page' #생략가능


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html' #생략가능
    pk_url_kwarg = 'post_id'
    context_object_name = 'post' #생략가능


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html' #생략가능

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html' #생략가능
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id':self.object.id})


class PostDeleteview(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html' #생략가능
    pk_url_kwarg = 'post_id'
    context_object_name = 'post' #생략가능

    def get_success_url(self):
        return reverse('post-list')


