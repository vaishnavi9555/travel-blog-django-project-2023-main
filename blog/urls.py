from django.urls import path
from . import views

urlpatterns = [
    path('article/form', views.article_form, name='article_form'),
    path('htmx/category/process',views.process_article,name='process_article'),
    path('htmx/tag/process',views.process_tag,name='process_tag'),
    path('htmx/article/list',views.article_list,name='article_list'),
    path('htmx/category/list',views.category_list,name='category_list'),
    path('htmx/tag/list',views.tag_list,name='tag_list'),
]