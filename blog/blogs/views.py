from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from blogs.forms import BlogPostForm
from blogs.models import BlogPost


class BlogPostIndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    model = BlogPost
    paginate_by = 10


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blogs/detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'post_slug'


class BlogPostCreateView(generic.CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogs/create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogPostUpdateView(generic.UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blogs/update_post.html'
    slug_url_kwarg = 'post_slug'
    slug_field = 'slug'
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return HttpResponseForbidden("Вы не можете редактировать этот пост.")
        return super().dispatch(request, *args, **kwargs)


class LoginUserView(LoginView):
    template_name = "blogs/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')


class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "blogs/register.html"
    success_url = reverse_lazy('login')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("index")
