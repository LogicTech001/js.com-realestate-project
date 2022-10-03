from django.contrib import admin

from pages.views import accodition, tilesfix
from .models import Electrical, Furniture, Plumbing, Painting , Tilesfix , Furniture , Accodition



# Register your models here.

admin.site.register(Plumbing)
admin.site.register(Painting)
admin.site.register(Tilesfix)
admin.site.register(Electrical)
admin.site.register(Furniture)
admin.site.register(Accodition)

    