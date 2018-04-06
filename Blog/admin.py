from django.contrib import admin
from Blog import models
# Register your models here.


@admin.register(models.User)
class AdminUser(admin.ModelAdmin):
    pass


@admin.register(models.Article)
class AdminArtical(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class AdminTag(admin.ModelAdmin):
    pass