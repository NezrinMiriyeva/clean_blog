from django.contrib import admin
from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ["name","url","order"]

# Register your models here.
admin.site.register(Profile)
admin.site.register(WebsiteCommon)
admin.site.register(HeaderSection)
admin.site.register(Menu,MenuAdmin)
admin.site.register(FooterIcon)
admin.site.register(Articles)
admin.site.register(Abouts)
# admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(ContactUs)




# Register your models here.
