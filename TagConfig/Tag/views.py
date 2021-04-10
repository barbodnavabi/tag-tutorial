from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from .models import Post
from .forms import PostForm
from taggit.models import Tag
from django.views.generic import DetailView

def home_view(request):
    posts = Post.objects.all()
    # Show most common tags 
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home.html', context)

def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'detail.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)



class TagDetailView(DetailView):
    model = Tag
    template_name = "detail.html"
    context_object_name='tags'
    def get_context_data(self, **kwargs):
        slug=self.kwargs['slug']
        tag = get_object_or_404(Tag, slug=slug)
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(tags=tag)

        return context
    