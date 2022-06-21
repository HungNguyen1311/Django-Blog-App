from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.list, name='blog'),
    path('<int:id>',views.blog_details, name='post'),
    path('login/',auth_views.LoginView.as_view(template_name='pages/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/blog'),name='logout'),
    path('add_blog/',views.add_blog, name='add_blog'),
    path('save_blog/',views.save_blog, name='save_blog'),
    path('blog_manage/',views.blog_manage, name='blog_manage'),
    path('blog_edit/<int:id>',views.blog_edit, name='blog_edit'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>',views.delete_post, name='delete_post'),
    path('hide_post/<int:id>',views.hide_post, name='hide_post'),
    path('show_post/<int:id>',views.show_post, name='show_post'),
    path('add_comment/',views.add_comment, name='add_comment'),
    path('delete_comment/<int:id>',views.delete_comment, name='delete_comment'),
    path('search_blog/',views.search_blog, name='search_blog'),
]