from django.db import models

# Create your models here.
# menu category
# menu

class Menu_Category(models.Model):
    menu_category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.menu_category_name
    
    class menu:
        verbose_name_plural = "Menu Categories"

class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.CharField()
    category = models.ForeignKey(Menu_Category, on_delete=models.PROTECT, default= None)

    def __str__(self):
        return self.menu_item
    
    class menu:
        verbose_name_plural = "Menus"
    
    
    
