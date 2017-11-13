from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .forms import PostForm
from django.contrib import messages


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST or None)
    context={
        "form":form,
    }
    if form.is_valid():
        instance=form.save(commit=False)
        title=form.cleaned_data.get("title")
        content=form.cleaned_data.get("content")
        instance.title=title
        instance.content=content
        instance.save()
        return HttpResponseRedirect(reverse('post_list'))

    return render(request,"create.html",context)

def post_list(request):
    list=Post.objects.all().order_by("-timestamp")
    context={
        "list": list,
    }
    return render(request, "post_list.html", context)


def post_display(request, post_id):
    display = get_object_or_404(Post, id=post_id)
    context = {
        'display': display,
    }
    return render(request, 'post_display.html', context)


def post_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
	    instance = form.save(commit=False)
	    instance.save()
	    messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
	    return HttpResponseRedirect(instance.get_absolute_url())

    context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
    return render(request, "create.html", context)



def post_delete(request, pk=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, pk=pk)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("/")
