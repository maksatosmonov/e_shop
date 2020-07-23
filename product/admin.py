from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    model = Product
    # fields = ["name", "user", "category","price", "active", "deleted"]
    readonly_fields = ["user", "quantity", "price", "active", "deleted"]
    list_display = [field.name for field in Product._meta.get_fields()]
    list_display_links = ["name", "user"]
    list_editable = ["price", "category", "active"]
    search_fields = ["name", "description", "user__username"]
    list_filter = ["category", "price", "active"]
    list_per_page = 5

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ["name", "age_limit", "active", "description"]
    list_display_links = ["name"]
    list_editable = ["age_limit", "active", "description"]



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
