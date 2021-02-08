from django.contrib import admin
from .models import Tag, Artist, Label
# Register your models here.
admin.site.register(Tag)
admin.site.register(Artist)
# admin.site.register(Album)
admin.site.register(Label)