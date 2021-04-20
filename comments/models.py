from django.db import models
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
    """Comments made on a specific product"""
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('shopping.Product', on_delete=models.CASCADE, related_name='comments')
    rating = models.SmallIntegerField(null=False, blank=False, default=4)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })

    def get_delete_url(self):
        return reverse('comment_delete', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })

    def get_update_url(self):
        return reverse('comment_update', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })