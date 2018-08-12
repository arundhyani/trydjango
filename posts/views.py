from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from urllib.parse import quote_plus

from .models import Post 
from .forms import PostForm
# Create your views here.
 

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if(request.method == 'POST') :
        print(request.POST.get("content"))
        print(request.POST.get("title"))
    form = PostForm(request.POST or None ,request.FILES or None)
    if(form.is_valid()) :
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form":form}
    return render(request, "post_form.html", context)

def post_detail(request,id=None): #retrieve
    instance = get_object_or_404(Post,id=id)
    share_string = quote_plus(instance.content)
    print("postdetail",share_string)
    context = {"obj": instance,
               "title" : instance.title,
               "share_string " : share_string,
               }
    return render(request, "post_detail.html", context)



def post_list(request): #list items
    posts_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts_list, 4) # Show 25 contacts per page
    page_var = "page"
    page = request.GET.get(page_var)
    try:
        objects_list = paginator.page(page)
    except PageNotAnInteger :
        objects_list = paginator.page(1)
    except EmptyPage :
        objects_list = paginator.page(paginator.num_pages)

    context = {
            "objects_list" : objects_list,
            "title" :  "List",
            "page_var" : page_var
            }
#    print(context['objects_list'],'\n','\n','\n')
    return render(request, "post_list.html", context)


def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if(form.is_valid()) :
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully updated")
        print(1,2,3,4,5,'\n','\n','\n','\n','\n')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {"form":form,
            "instance":instance,
            "title":instance.title
            }
    return render(request, "post_form.html", context)


def post_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    instance.delete()
#    messages.success(request,"Successfully deleted")
    return redirect('posts:postslist')
