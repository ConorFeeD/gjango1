from django.contrib import admin
from news.models import *

admin.site.register(News)
admin.site.register(Question)
admin.site.register(Choice)