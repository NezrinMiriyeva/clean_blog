from django.urls import path
from .views import index, about, post_detail_view, contact
from .views import login_page, login_view, register, dashboard


urlpatterns = [
     path("", index, name= "home-page"),
     path("login/", login_page, name= "login-page"),
     path("login-view/", login_view, name="login"),
     path("register/", register, name="register"),
     path("dashboard/", dashboard, name="dashboard"),
     # path('article/', ArticleListView.as_view(), name="list_view"),
     # path('article/<int:pk>/detail/', ArticleDetailView.as_view(), name="detail_view"),
     # path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name="update_view"),
     # path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name="delete_view"),
     # path('article/new', ArticleCreateView.as_view(), name="create_view")
     path("about/", about, name="about"),
     path("post/<int:id>/", post_detail_view, name="post"),
     path("contact/", contact, name="contact"),
     # path("logout/", logout_view, name="logout"),
     # path("dashboard/", dashboard, name="dashboard"),
     # path("author/<int:id>/", author_name, name="author"),

]