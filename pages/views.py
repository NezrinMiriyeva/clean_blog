from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import WebsiteCommon, HeaderSection, Menu, FooterIcon, Articles, Abouts, Contact
from django.core.paginator import Paginator
from .forms import ContactForm



def common_data():
    context = {}
    context["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()
    context["footer_list"] = FooterIcon.objects.all()
    return context

def index(request):
    context = common_data()
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


def post(request):
    context = {}
    all_object = Articles.objects.all()
    paginator = Paginator(all_object, 3)
    page = 1
    if request.GET.get("page"):
        context["news_list"] = paginator.get_page(request.GET.get("page"))
    else:
        context["news_list"] = paginator.get_page(1)
    context["page_range"] = list(paginator.page_range)[0 if page < 3 else page - 3:page + 3]

    context["pagination"] = paginator
    return render(request, "post.html", context)


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

def test_view(request):
    if request.user.is_authenticated:
        return HttpResponse("login olmush user")
    else:
        return HttpResponse("login olmayib")
