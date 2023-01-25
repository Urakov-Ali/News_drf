from django.db import models


class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class New(models.Model):
    title = models.ForeignKey(Title, blank=False, null=True, on_delete=models.SET_NULL)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.author

    # class Meta:
    #     ordering = ['-date']
