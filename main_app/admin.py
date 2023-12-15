from django.contrib import admin


from .models import Vinyl, Concert, Genre

admin.site.register(Vinyl)
admin.site.register(Concert)
admin.site.register(Genre)