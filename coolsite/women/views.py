from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *
# Create your views here.


class WomenHome(DataMixin, ListView):
    paginate_by = 2
    model = Women
    template_name = 'women/main_page.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)
# def main_page(request):  # HttpRequest
#     posts = Women.objects.all()
#     dictionary_main_page = {'posts': posts, 'menu': menu, 'title': 'Главная страница', 'cat_selected': 0}
#     return render(request, 'women/main_page.html', context=dictionary_main_page)

@login_required
def about(request):  # HttpRequest
    # return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})
    return HttpResponse("О сайте1")


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/add_page.html', {'form': form, 'menu': menu, 'title': "Добавление статьи"})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))
# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     dictionary_post = {'post': post,
#                         'menu': menu,
#                         'title': post.title,
#                         'cat_selected': post.cat_id}
#
#     return render(request, 'women/post.html', context=dictionary_post)


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/main_page.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))
# def show_category(request, cat_slug):
#     category = Category.objects.filter(slug=cat_slug)
#     posts = Women.objects.filter(cat_id=category[0].id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     dictionary_category = {'posts': posts,
#                             'menu': menu,
#                             'title': 'Отображение по рубрикам',
#                             'cat_selected': category[0].id}
#
#     return render(request, 'women/main_page.html', context=dictionary_category)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h2>')