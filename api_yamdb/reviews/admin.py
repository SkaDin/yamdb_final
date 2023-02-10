from django.contrib import admin
from reviews.models import Category, Comments, Genre, Review, Title

admin.site.register(Review)
admin.site.register(Comments)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
