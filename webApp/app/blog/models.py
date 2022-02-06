from time import timezone
from django.db import models
from django.conf import settings
from django.utils import timezone
#NLP
from nrclex import NRCLex

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify



User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self.db)

    def published(self):
        return self.get_queryset().published()

# Create your models here.
class BlogPost(models.Model):

    user = models.ForeignKey(User, null=True, default = 1 , on_delete=models.SET_NULL)

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    content = MarkdownxField(blank=True, null=True)

    publish_date = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects=BlogPostManager()

    class Meta:
        ordering=['-publish_date', 'updated', 'timestamp']

    def get_publish_date(self):
        if self.publish_date == None :
            return "Draft Post"    
        else:
            return self.publish_date

    def is_published(self):
        return self.publish_date != None

    def publish(self):
        self.publish_date = timezone.now()
    
    def unpublish(self):
        self.publish_date = None

    def get_absolute_url(self):
        return f'/blog/{self.slug}'
    
    def get_edit_url(self):
        return f'/blog/{self.slug}/edit'

    def get_delete_url(self):
        return f'/blog/{self.slug}/delete'

    def processContentwithNRCLex(self):
        text = self.content

        emotion = NRCLex(text)
        return emotion

    # Create a property that returns the markdown 
    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    



