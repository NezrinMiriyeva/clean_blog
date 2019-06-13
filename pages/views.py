from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from .models import Articles
# from .forms import Articleform
from django.urls import reverse_lazy
from .models import WebsiteCommon, HeaderSection, Menu, FooterIcon, Articles, Abouts, Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, RegistrationUserForms
from .models import Profile


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

# #
# def author_name(request,id):
#     context = common_data()
#     context["author"] = AuthorProfile.objects.filter(id=id).last()
#     return render(request, "author.html", context)

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


# def logout_view(request):
#     logout(request)
#     return redirect("login-page")

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
    context["user_list"] = Profile.objects.all()
    return render(request, "dashboard.html", context)

# class HomePage(generic.TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = {}
#         return context
# #
# class ArticleListView(generic.ListView):
#     model = Articles
#     template_name = "post.html"
# #
# class ArticleDetailView(generic.DetailView):
#     model = Articles
#     template_name = "article_detail.html"
#
# class ArticleUpdateView(generic.UpdateView):
#     model = Articles
#     template_name = "article_form.html"
#     form_class = Articleform
#     success_url = reverse_lazy("list_view")
