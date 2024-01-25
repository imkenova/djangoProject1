from django.views.generic import ListView, TemplateView, CreateView
from .models import Post

from .form import PostForm



class BlogList(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class AboutPageView(TemplateView):
    template_name = 'about.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


