from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from django.utils import timezone
# Create your models here.
blog_cate_choices=(
    ('Sport','Sport'),
    ('Social','Social'),
    ('Cars','Cars'),
    ('Mobile','Mobile'),
    ('News','News'),
    ('Gamming','Gamming')
)
class Post(models.Model):
    blog_cate=models.CharField(max_length=255, null=True, choices=blog_cate_choices)
    title=models.CharField(max_length=100)
    image=models.ImageField(null=True, blank=True)
    content= RichTextUploadingField(blank=True)
    date=models.DateTimeField(auto_now_add=True)
    accountid=models.IntegerField(max_length=11,)
    showblog=models.IntegerField(max_length=1)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    username=models.CharField(max_length=100)
    text_content=models.CharField(max_length=1020)
    date_comment=models.DateTimeField(auto_now_add=True)
    blog_id=models.IntegerField(max_length=1, null=True)
    show_comment=models.IntegerField(max_length=1)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)