from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name","url","order"]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["name","author"]
    list_filter = ["author"]

# Register your models here.
admin.site.register(Profile)
admin.site.register(WebsiteCommon)
admin.site.register(HeaderSection)
admin.site.register(Menu,MenuAdmin)
admin.site.register(FooterIcon)
admin.site.register(Articles,ArticleAdmin)
admin.site.register(Abouts)
admin.site.register(Login)
admin.site.register(Contact)
admin.site.register(ContactUs)
admin.site.register(Settings)



# Register your models here.
