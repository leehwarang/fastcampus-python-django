from django.db import models

# Create your models here.

#ORM을 통해 database를 관리

class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title + str(self.create_date)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.PROTECT,
        null = True
    )
    text = models.CharField(max_length = 200)
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.text[:13] + '...' if len(self.text) > 13 else self.text
