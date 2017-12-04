from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from blog.models import Blog, Category
from django.http import Http404
from django.utils.translation import ugettext as _


class PostDetail(DetailView):
    template_name = 'blog/detail.html'
    model = Blog

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        obj = super(PostDetail, self).get_object(queryset=queryset)
        if obj.author.username == self.kwargs['username']:
            return obj
        else:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})


class CategoryView(ListView):
    """List blog posts that all have the same category."""

    model = Blog
    template_name = 'blog/category.html'

    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        get_object_or_404(Category, name=self.kwargs['category'])
        qs = qs.filter(categories__name=self.kwargs['category'])
        return qs
