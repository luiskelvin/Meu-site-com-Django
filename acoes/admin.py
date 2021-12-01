from django.contrib import admin

from .models import Filmes, Series, HQs, Opinioes, Noticias

admin.site.register(Filmes)
admin.site.register(Series)
admin.site.register(HQs)
admin.site.register(Noticias)
admin.site.register(Opinioes)