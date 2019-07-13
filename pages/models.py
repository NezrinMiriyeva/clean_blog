from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class WebsiteCommon(models.Model):
    brand = models.CharField(max_length=255)
    copyright_text = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.brand)

class HeaderSection(models.Model):
    background_image = models.ImageField(upload_to="header/")
    main_title = models.CharField(max_length=255)
    sub_title = models.TextField()

    def __str__(self):
        return"{}".format(self.main_title)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return"{}".format(self.name)

    class Meta:
        ordering = ("order",)

class FooterIcon(models.Model):
    icon = models.CharField("icon", max_length=255, null=True, blank=True)
    link = models.TextField()

    def __str__(self):
        return "{}".format(self.icon)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/", null=True, blank=True)
    background_image = models.ImageField(upload_to="profile/", null=True, blank=True)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_background_image(self):
        if self.background_image:
            return self.background_image.url
        else:
            return ""

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Articles(models.Model):
    name = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255,null=True, blank=True )
    content = RichTextUploadingField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    background_image = models.ImageField(upload_to="article/", null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return "{}".format(self.name)

    def get_image(self):
        if self.background_image:
            return self.background_image.url
        else:
            return ""

class Abouts(models.Model):
    sub_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    background_image = models.ImageField(upload_to="about/")


class Contact(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to="contact/", null=True, blank=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Login(models.Model):
    background_image = models.ImageField(upload_to="login/", null=True, blank=True)

class Settings(models.Model):
    background_image = models.ImageField(upload_to="settings/", null=True, blank=True)

    def get_image(self):
        if self.background_image:
            return self.background_image.url
        else:
            return ""