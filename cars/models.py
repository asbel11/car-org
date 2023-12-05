from django.db import models
from django.urls import reverse 

class Cars(models.Model):
    title = models.CharField(max_length=2000)
    author = models.ForeignKey(
        "auth.User", 
        on_delete=models.CASCADE,)
    image = models.ImageField(null=True, blank=True,upload_to="images/")

    
    body = models.TextField()
    
    def __str__(self): 
        return self.title
    def get_absolute_url(self): 
        return reverse("post_detail", kwargs={"pk": self.pk}) 



