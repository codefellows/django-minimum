from django.views.generic import ListView
from blog.models import Blog


class HomeView(ListView):
    """View for listing all of the blog objects."""

    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'posts'
