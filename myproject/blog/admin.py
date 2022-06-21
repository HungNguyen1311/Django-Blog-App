from django.contrib import admin
from .models import Post, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=['username','blog_id','text_content','date_comment']
    search_fields=['username']
admin.site.register(Comment, CommentAdmin)