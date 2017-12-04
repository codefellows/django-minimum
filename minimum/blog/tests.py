from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog


class BlogTests(TestCase):
    def setUp(self):
        self.user = User(username='flerg', email='flerg@blerg.merg')
        self.user.set_password('potatoes')
        self.user.save()

    def test_whenever_post_saved_with_published_status_date_is_set(self):
        blog = Blog(title='Words and stuff', body='', author=self.user, status='draft')
        blog.save()
        self.assertIsNone(blog.date_published)
        blog.status = 'published'
        blog.save()
        self.assertIsNotNone(blog.date_published)
