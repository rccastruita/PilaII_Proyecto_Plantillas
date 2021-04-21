from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Comment(models.Model):
    """Comments made on a specific product"""
    # Author of the comment
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    # Product on which the comment was made
    product = models.ForeignKey('shopping.Product', on_delete=models.CASCADE, related_name='comments')
    # Text of the comment
    body = models.TextField()
    # When the comment was last edited (or created)
    timestamp = models.DateTimeField(auto_now=True)
    # Rating given to the product (From 1 to 5)
    rating = models.SmallIntegerField(
        null=False, 
        blank=False,
        default=3,
        choices=[
            (1, 'Terrible'),
            (2, 'Malo'),
            (3, 'Regular'),
            (4, 'Bueno'),
            (5, 'Excelente'),
        ]
    )

    # For use in detail view
    def get_absolute_url(self):
        return reverse('comment_detail', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })

    # For use in DeleteView
    def get_delete_url(self):
        return reverse('comment_delete', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })

    # For use in UpdateView
    def get_update_url(self):
        return reverse('comment_update', kwargs={
            'product_pk': self.product.pk,
            'comment_pk': self.pk,
        })