from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, get_object_or_404, redirect
from blog.models import BlogPost

from .forms import BlogForm, BlogModelForm

# Create your views here.
# CRUD - Create, Retrieve, Update, Delete


template_detail = "blog/page.html" 
template_create = "blog/create.html"
template_list = 'blog/list.html'


# List Objects
def blogpost_list_view(request):
    # query
    qs = BlogPost.objects.all()

    title = "All Blogs"
    context = {'object_list': qs, "action":"blogs", "title":title}

    return render(request, template_list, context)

# create 1 object
@login_required
def blogpost_create_view(request):
    message = ""

    form = BlogModelForm(request.POST or None)
    if form.is_valid():
        # add object to database
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogForm()
        message = "Thank you for creating a blog"
        return redirect('detail', slug=obj.slug)

    context = {'message':message,'title' : "Create your Blog", 'form': form}
    return render(request, template_create, context)

# retrieve 1 object
def blogpost_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    editable = request.user == obj.user
    context = {"name" : request.user, "blog":obj, "editable":editable}

    emotion = obj.processContentwithNRCLex()
    print('\n', emotion.words)
    print('\n', emotion.sentences)
    print('\n', emotion.affect_list)
    print('\n', emotion.affect_dict)
    print('\n', emotion.raw_emotion_scores)
    print('\n', emotion.top_emotions)
    print('\n', emotion.affect_frequencies)

    return render(request, template_detail, context)


# update 1 object
@login_required
def blogpost_update_view(request, slug):
    template = "blog/update.html" 
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogModelForm(request.POST or None, instance=obj)
    message = ""

    editable = request.user == obj.user
    #only creator and staff can modify
    if not editable and not request.user.is_staff:
        raise Exception("Invalid User")
    
    if form.is_valid():
        message = "Blog updated successfully"
        obj = form.save()

        return redirect('detail', slug=obj.slug)

    # Updated page
    title = f"Update Blog {obj.title}"
    context = {"message": message, "title" :  title, "form": form, "user":obj.user, "blog":obj}

    return render(request, template, context)

# delete 1 object
@login_required
def blogpost_delete_view(request, slug):
    
    obj = get_object_or_404(BlogPost, slug=slug)
    template = "blog/delete.html" 
    context = {"name" : request.user, "blog":obj}

    if request.method== "POST":
        obj.delete()
        return redirect("/blog")

    return render(request, template, context)