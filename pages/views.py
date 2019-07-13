from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .forms import LoginForm, UserSettingsForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from .models import WebsiteCommon, HeaderSection, Menu, FooterIcon, Articles, Abouts, Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, RegistrationUserForms, Articleform
from .models import Profile,Settings


def common_data():
    context = {}
    context["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()
    context["footer_list"] = FooterIcon.objects.all()
    return context

def index(request):
    context = common_data()
    context["register_form"] = RegistrationUserForms()
    context["login_form"] = LoginForm()
    all_object = Articles.objects.all()
    paginator = Paginator(all_object, 3)
    page = 1
    if request.GET.get("page"):
        context["article_list"] = paginator.get_page(request.GET.get("page"))
    else:
        context["article_list"] = paginator.get_page(1)
    context["page_range"] = list(paginator.page_range)[0 if page < 3 else page - 3:page + 3]

    context["pagination"] = paginator
    context["about_list"] = Abouts.objects.all()
    context["contact_list"] = Contact.objects.all()

    return render(request, "index.html", context)

# Create your views here.

def about(request):
    context = common_data()
    context["abouts"] = Abouts.objects.last()
    return render(request, "about.html", context)

def post_detail_view(request, id):
    context = common_data()
    context["post"] = Articles.objects.filter(id=id).last()
    return render(request, "post.html", context)

def contact(request):
    context = common_data()
    context["contact"] = Contact.objects.last()
    context["form"] = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.info(request, "Ugurla elave olundunuz")
            form.save()
        else:
            messages.error(request, "Form duzgun deyil {}".format(form.errors.as_text))

            return redirect("home-page")
    return render(request, "contact.html", context)


def author_name(request,id):
    context = common_data()
    context["profile"] = Profile.objects.filter(id=id).last()
    all_object = Articles.objects.filter(author_id = id)
    paginator = Paginator(all_object, 5)
    page = 1
    if request.GET.get("page"):
        context["article_list"] = paginator.get_page(request.GET.get("page"))
    else:
        context["article_list"] = paginator.get_page(1)
    context["page_range"] = list(paginator.page_range)[0 if page < 5 else page - 5:page + 5]

    context["pagination"] = paginator
    return render(request, "author.html", context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    context = common_data()
    context["form"] = LoginForm()
    return render(request,"login.html",context)

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Bele bir istifadeci yoxdur")
                return redirect("login-page")
        else:
            messages.error(request, "Form duzgun deyil")
    else:
        return redirect("login-page")

def register(request):
    if request.method == "POST":
        form = RegistrationUserForms(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get("password"))
            user.save()
            Profile.objects.create(
                image=request.FILES["image"],
                user=user
            )
            messages.success(request, "ugurla qeydiyyatdan kecdiniz")
            return redirect("login-page")
        else:
            messages.error(request, "Form duzgun deyil {}".format(form.errors.as_text))

        return redirect("login-page")
    else:
        context = common_data()
        context["register_form"] = RegistrationUserForms()
        return render(request, "register.html", context)

@login_required(login_url="/")
def dashboard(request):
    context = common_data()
    context["article_list"] = Articles.objects.filter(author__user=request.user)
    return render(request, "dashboard.html", context)

class ArticleUpdateView(generic.UpdateView):
    model = Articles
    template_name = "article_form.html"
    form_class = Articleform
    success_url = reverse_lazy("dashboard")

    def get_queryset(self):
        qs = super(ArticleUpdateView, self).get_queryset()
        return qs.filter(author=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data(**kwargs)
        context = {**context, **common_data()}
        return context

class ArticleDeleteView(generic.DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("dashboard")
    
    def get_queryset(self):
        qs = super(ArticleDeleteView, self).get_queryset()
        return qs.filter(author=self.request.user.profile)

class ArticleCreateView(generic.CreateView):
    model = Articles
    form_class = Articleform
    template_name = "article_create.html"
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user.profile
        article.save()
        return super(ArticleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ArticleCreateView, self).get_context_data(**kwargs)
        context = {**context, **common_data()}
        return context

def logout_view(request):
    logout(request)
    return redirect("login-page")

class UserSettings(generic.FormView):
    form_class = UserSettingsForm
    template_name = "user-settings.html"
    success_url = "/"

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'instance': self.request.user
        }

        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def form_valid(self, form):
        if self.request.user.check_password(self.request.POST.get("password")):
            form.instance = self.request.user
            form.save()
            return super(UserSettings, self).form_valid(form)
        else:
            return HttpResponse("not")

    def form_invalid(self,form):
        a = 2
        return super(UserSettings, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(UserSettings,self).get_context_data(**kwargs)
        if self.request.method == "GET":
            context["settings"] = Settings.objects.last()
            context["form"] = UserSettingsForm(instance=self.request.user)
        return context

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserSettings, self).dispatch(request)