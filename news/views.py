from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news/news_list.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'post' # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')  # От ранней к поздней
    paginate_by = 1
    form_class = PostForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    template_name = 'news/news_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'news/news_create.html'
    form_class = PostForm
    success_url = '/news/'


class PostDetail(DetailView):
    model = Post
    template_name = 'news0.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    template_name = 'news/news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
