from django.contrib import admin
from tree.models import *
# Register your models here.



@admin.register(Tree)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(TreeImplementation)
class AuthorAdmin(admin.ModelAdmin):
    pass