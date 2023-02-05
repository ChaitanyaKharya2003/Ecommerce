from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key= True)
    tilte = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    date = models.DateField()
    thumbnail = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        self.pub_date = now()
        return self.tilte
    
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blogpost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username