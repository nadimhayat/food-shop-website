from django.db import models

# class Category(models.Model):
#     title = models.CharField(max_length=120,db_index=True) #veg, non-veg
#     slug = models.SlugField(max_length=120,db_index=True)

#     # class Meta:
#     #     ordering=('name', )
#     #     verbose_name = 'category'
#     #     verbose_name_plural = 'categories'
#     def __str__(self):
#         return self.title

class ProductDetail(models.Model):
    # category = models.ForeignKey('Category', related_name='productdetails', null=True, blank=True)
    name = models.CharField(max_length=120,db_index=True)
    thumb = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(blank=True)
    price = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    available = models.CharField(max_length=120,db_index=True)
    category = models.CharField(max_length=120,db_index=True)
    subcategory = models.CharField(max_length=120,db_index=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name