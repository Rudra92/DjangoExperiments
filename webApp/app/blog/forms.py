from django import forms

from blog.models import BlogPost
from markdownx.fields import MarkdownxFormField


class BlogForm(forms.Form):
    title = forms.CharField(required=True)
    slug = forms.SlugField(required=True)
    content = MarkdownxFormField(widget=forms.Textarea, required=True)


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    def clean_title(self):
        data = self.cleaned_data["title"]
        instance = self.instance

        qs = BlogPost.objects.filter(title__iexact=data)
        # do not account for this instance if we are updating
        if  instance is not None:
            qs = qs.exclude(pk=instance.pk) # check primary key

        # check if title already exists
        if qs.exists():
            raise forms.ValidationError("Title provided already exists. Please choose another one.")
        
        return data
        