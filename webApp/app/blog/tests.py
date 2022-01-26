

from turtle import title
from django.test import TestCase
from .models import BlogPost

from django.contrib.auth import get_user_model

User = get_user_model()


class PostTestCase(TestCase):



    def testPost(self):

        user = User.objects.create_user(username='testuser', password='12345')

        dict = {"user":user,"title":"Title", "slug":"test-case", "content":"Create Blog Test" }
        post = BlogPost(**dict )
        self.assertEqual(post.user, dict["user"])
        self.assertEqual(post.title, dict["title"])
        self.assertEqual(post.slug, dict["slug"])
        self.assertEqual(post.content, dict["content"])
        
