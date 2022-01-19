from django.db import models
from django.conf import settings

#NLP
from nrclex import NRCLex

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify



User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):

    user = models.ForeignKey(User, null=True, default = 1 , on_delete=models.SET_NULL)

    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    #content = models.TextField(null=True, blank=True)
    content = MarkdownxField(blank=True)


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

    



