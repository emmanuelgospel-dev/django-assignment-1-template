from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from .models import BlogPost
from .forms import BlogForm


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    category = request.GET.get('category')
    if category:
        posts = posts.filter(category=category)
    context = {
        'posts': posts,
        'categories': BlogPost.CATEGORY_CHOICES,
        'active_category': category,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    # increment views_count without a race-condition-prone read-modify-write
    BlogPost.objects.filter(pk=post.pk).update(views_count=F('views_count') + 1)
    post.refresh_from_db()
    return render(request, 'blog/blog_detail.html', {'post': post})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post published.')
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form, 'mode': 'create'})


@login_required
def blog_update(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated.')
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form, 'mode': 'edit', 'post': post})


@login_required
def blog_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})
