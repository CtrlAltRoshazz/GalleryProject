from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    uploaded_by = models.CharField(max_length=100 , default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(CategoryModel , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')