from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm, EditPost

def blog_details(request, id):
    post=Post.objects.get(id=id)
    comments=Comment.objects.filter(blog_id=id).order_by("-date_comment")
    number=Comment.objects.filter(blog_id=id).order_by("-date_comment").count()
    return render(request, 'pages/blog-details.html',{'post':post,'comments':comments,'number':number})
def list(request):
    post=Post.objects.filter(showblog=1).order_by("-date")
    banner=Post.objects.filter(showblog=1).order_by("-date")[:4]
    return render(request, 'pages/home.html', {'post':post,'banner':banner})
def add_blog(request):
    if request.method=='POST':
      blog_cate=request.POST['blog_cate']
      author_id = request.user.id
      title = request.POST['title']
      image = request.FILES['image']
      content = request.POST['content']
      showblog = request.POST['showblog']
      post = Post.objects.create(blog_cate=blog_cate,title=title, image=image, content=content, showblog=showblog, accountid=author_id)
      post.save()
      return redirect('/blog/add_blog')
    else:
        form = PostForm()
        return render(request, 'pages/add_blog.html',{'form':form})
    # form = PostForm()
    # return render(request, 'pages/add_blog.html',{'form':form})
def save_blog(request):
    if request.method=='POST':
        author_id=request.POST['post_author_id']
        title=request.POST['post_title']
        image=request.FILES['post_image']
        content=request.POST['post_content']
        showblog=request.POST['post_status']
        post=Post.objects.create(title=title,image=image,content=content,showblog=showblog,accountid=author_id)
        post.save()
        return redirect('/blog/add_blog')
    # else:
def blog_manage(request):
    post=Post.objects.filter(accountid=request.user.id).order_by("-date")
    return render(request, 'pages/blog_manage.html',{'post':post})
def blog_edit(request, id):
    post=Post.objects.get(id=id)
    comments = Comment.objects.filter(blog_id=id).order_by("-date_comment")
    number = Comment.objects.filter(blog_id=id).order_by("-date_comment").count()
    return render(request, 'pages/blog-edit.html',{'post':post,'comments':comments,'number':number})

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method=='POST':
      blog_cate=request.POST['blog_cate']
      title = request.POST['title']
      image = request.FILES.get('image', None)
      content = request.POST['content']
      showblog = request.POST['showblog']

      get_post=Post.objects.get(id=id)
      get_post.blog_cate=blog_cate
      get_post.title=title
      if(image == None):
        get_post.image=get_post.image
      else:
        get_post.image=image
      get_post.content=content
      get_post.showblog=showblog
      get_post.save()
      # Post.objects.filter(pk=id).update(title=title, image=image, content=content, showblog=showblog)
      return redirect('/blog/blog_edit/'+str(id))
    else:
        form = PostForm(instance=post)
        return render(request, 'pages/edit_post.html',{'post':post,'form':form})
    # form = PostForm()
    # return render(request, 'pages/add_blog.html',{'form':form})
def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/blog_manage/')
def hide_post(request,id):
    post = Post.objects.get(id=id)
    post.showblog=0
    post.save()
    return redirect('/blog/blog_edit/' + str(id))
def show_post(request,id):
    post = Post.objects.get(id=id)
    post.showblog=1
    post.save()
    return redirect('/blog/blog_edit/' + str(id))
def add_comment(request):
    if request.method == 'POST':
        if(request.user.username):
            username=request.user.username
        else:
            username = request.POST['username']
        blogid=request.POST['postid']
        text_content = request.POST['text_content']
        showcomment = 1
        comment = Comment.objects.create(username=username,text_content=text_content, show_comment=showcomment, blog_id=blogid)
        comment.save()
        return redirect('/blog/' + str(blogid))
def delete_comment(request, id):
    comment=Comment.objects.get(id=id)
    blog_id=comment.blog_id
    comment.delete()
    return redirect('/blog/'+ str(blog_id) )
def search_blog(request):
    post_name=request.POST['blog_name']
    post=Post.objects.filter(title__contains=post_name,showblog=1)
    return render(request, 'pages/search_blog.html', {'post': post})