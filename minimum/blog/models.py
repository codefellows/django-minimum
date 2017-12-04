from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __repr__(self):
        return f"<Category { self.name }>"

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Model for blog posts."""
    title = models.CharField(max_length=256)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, related_name='posts')
    categories = models.ManyToManyField(Category)
    STATUSES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('private', 'Private')
    ]
    status = models.CharField(choices=STATUSES, max_length=10, default="draft")

    def __repr__(self):
        return f"<Blog Post { self.title }>"

    def __str__(self):
        return self.title


@receiver(post_save, sender=Blog)
def change_publication_status(instance, **kwargs):
    """When a blog post instance is saved, if it's newly published then set the publication date."""
    if not instance.date_published and instance.status == 'published':
        instance.date_published = datetime.now()
        instance.save()


# after a blog instance is saved, and date_published was not previously set,
# and the published status is now "published", set the date_published field to
# be right now


# blog = Blog()
# blog.author.username

# mike = User()
# mike.posts.all()
# mike.posts.filter_by(status='public').all()