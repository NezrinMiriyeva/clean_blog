from django.urls import path
from .views import index, about, post_detail_view, contact, test_view


urlpatterns = [
     path("", index, name= "home-page"),
     path("about/", about, name="about"),

     # path("basic/", basic, name="basic"),
     path("post/<int:id>/", post_detail_view, name="post"),
     path("contact/", contact, name="contact"),
     path("test/", test_view, name="test-view"),
]