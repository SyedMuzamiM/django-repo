from django.contrib import admin
from .models import NewsArticle

admin.site.site_header = 'threline'
admin.site.site_title  = 'threline admin'
admin.site.index_title = 'theline administration'
# admin.site.index_template = "templates/admin_index.html"

admin.site.register(NewsArticle)