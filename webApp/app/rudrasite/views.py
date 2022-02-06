from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

from blog.models import BlogPost

name = "Unknown"
# default context
context  = {"name" : name, "content":"Please log in to see blogs"}
    
def home_page(request):

    # default context
    template = "blog/list.html"
    title = "Last Published Blogs"

    qs = list(BlogPost.objects.published())[-5:]

    context = {"title": title, "object_list" : qs, "action":"home"}

    return render(request, template, context)

def about_page(request):
# default context

    template = "about.html"
    title="About Me"

    context = {"name" : request.user, "action":"about", "title":title}

    return render(request, template, context)
def contact_page(request):
# default context

    title = "Contact Me"
    template = "contact.html"

    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()

    context = {"title" : title, "form" : form, "action":"contact"}

    return render(request, template, context)





