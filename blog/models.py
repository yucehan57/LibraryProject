from django.db import models
from django.urls import reverse
from accounts.models import User


class Category(models.Model):
    """Represent a category for a blog post"""
    ###FIX VERBOSE NAME PLURAL
    name = models.CharField(max_length=50,
                help_text='Choose categories for the blog post', default=None)


    def __str__(self):
        """String representation of the Category Object"""
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, default=None)
    tags = models.ManyToManyField('Tag')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """url access to the detailed post page"""
        return reverse('blog:post-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-date_created']


class Tag(models.Model):
    name = models.CharField(max_length=155, default=None)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    # Consider default date add as False until comment approved (with method)
    date_commented = models.DateTimeField(auto_now_add=True)

    # def approve_comment(self):
    #     date_commented = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_commented']

    def __str__(self):
        return f'{self.post} by {self.user}'
