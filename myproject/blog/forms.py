from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=('blog_cate','title','image','content','showblog')

class EditPost(ModelForm):
    class Meta:
        model=Post
        fields=('blog_cate','title','image','content','showblog')