from django.contrib import admin
from my_app.models import Tag, Example

admin.site.register((Example, Tag))