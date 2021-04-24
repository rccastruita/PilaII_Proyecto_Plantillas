from django.test import TestCase, Client
from django.contrib import auth
import random

from users.models import User
from shopping.models import Product
from .models import Comment

def print_user(user):
    """ Print the given user to the console """
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Password: {user.password}")
    if user.city is not None:
        print(f"City: {user.city.pk} - {user.city}")
    else:
        print('City: None')
    print(f"In mailing list: {user.in_mailing_list}")
    print()

def print_product(product):
    """ Print the given product to the console """
    print(f"Product: {product.name}:")
    print(f"  Primary Key: {product.pk}")
    print(f"  URL: {product.get_absolute_url()}")
    print(f"  Category: {product.category}")
    print(f"  Description: {product.description if product.description else None}")
    print(f"  Image: {product.image if product.image else None}")
    print(f"  Comments: {product.comments.count()}")
    print()

def print_comment(comment):
    """ Print the given comment to the console """
    print(f"Comment {comment.pk}: ")
    print(f"  On: {comment.product}")
    print(f"  By: {comment.user}")
    print(f"  Rating: {comment.rating}")
    print(f"  Comment: {comment.body}")
    print()

# Create your tests here.
class CommentsTestCase(TestCase):
    def setUp(self):
        # Users
        User.objects.create_user(
            username = 'foo',
            email = 'foo@test_mail.com',
            password = 'foo16130789',
        )
        User.objects.create_user(
            username = 'bar',
            email = 'bar@test_mail.com',
            password = 'bar16130789',
        )

        # Raw passwords (for logins)
        self.raw_passwords = {
            'foo': 'foo16130789',
            'bar': 'bar16130789',
        }

        # Products
        Product.objects.create(
            name = 'My Product 1',
            description = 'Description of My Product 1 LoremIpsuuuuuuuuuum',
        )

        # Comments
        Comment.objects.create(
            user = User.objects.get(username='foo'),
            product = Product.objects.get(),
            rating = 4,
            body = 'Lorem ipsumasdflasdjnf',
        )

        # Test Client for http requests
        self.c = Client()

    def test_comments_view(self):
        """ Test if a product's DetailView Displays the product's comments """
        product = Product.objects.get()
        response = self.c.get(product.get_absolute_url())
        for i in Comment.objects.filter(product__exact=product):
            self.assertContains(response, i.body)

    def test_post_comment(self):
        """ Test if sending a POST request to the CommentCreateView creates a comment """
        product = Product.objects.get()
        initial_comment_count = product.comments.count()

        opinions = ['awful', 'bad', 'decent', 'good', 'awesome']
        for username, password in self.raw_passwords.items():
            self.c.login(username=username, password=password)

            user = auth.get_user(self.c)

            rating = random.randint(1, 5)
            response = self.c.post(product.get_new_comment_url(), {
                'user': user.pk,
                'product': product.pk,
                'rating': rating,
                'body': f"I, {user.username}, think that this product is {opinions[rating-1]}.",
            }, follow=True)
            self.assertRedirects(response, product.get_absolute_url())
            
        self.assertEqual(initial_comment_count + User.objects.count(), product.comments.count())

    def test_post_validation(self):
        """ TODO: Test validation for CommentCreateView """
        pass

    def test_comment_delete(self):
        """ Test if sending a POST request to a comment's DeleteView deletes the comment """
        self.c.login(username='foo', password=self.raw_passwords['foo'])
        
        user = auth.get_user(self.c)
        comment = Comment.objects.create(
            user = user,
            product = Product.objects.get(),
            rating = 3,
            body = 'This comment will be deleted.'
        )

        product = comment.product

        response = self.c.post(comment.get_delete_url(), follow=True)

        self.assertRedirects(response, product.get_absolute_url())
        self.assertNotIn(comment, Comment.objects.all())

    def test_comment_delete_validation(self):
        """ Test if only the comment's author can delete a comment 
        TODO: Also let superusers delete comments via this view """
        comment_foo = Comment.objects.create(
            user = User.objects.get(username='foo'),
            product = Product.objects.get(),
            rating = 5,
            body = 'Comment by foo'
        )
        comment_bar = Comment.objects.create(
            user = User.objects.get(username='bar'),
            product = Product.objects.get(),
            rating = 1,
            body = 'Comment by bar'
        )

        self.c.login(username='foo', password=self.raw_passwords['foo'])
        response_wrong_user = self.c.post(comment_bar.get_delete_url(), follow=True)

        self.assertEqual(response_wrong_user.status_code, 403)
        self.assertContains(response_wrong_user, '403 Forbidden', status_code=403)
        self.assertContains(response_wrong_user, 
            'No cuentas con los permisos suficientes para borrar comentarios de terceros.', 
            status_code=403
        )
        
        self.assertIn(comment_bar, Comment.objects.all())

        self.c.logout()
        response_anonymous = self.c.post(comment_foo.get_delete_url(), follow=True)

        self.assertRedirects(response_anonymous, '/users/login/?next='+comment_foo.get_delete_url())
        self.assertIn(comment_foo, Comment.objects.all())

    def test_comment_editing(self):
        """ Test the CommentUpdateView """
        product = Product.objects.get()
        user = User.objects.get(username='foo')
        comment = Comment.objects.create(
            user = user,
            product = product,
            rating = 3,
            body = 'Original comment',
        )

        new_rating = 5
        new_body = 'Edited comment'

        self.c.login(username='foo', password=self.raw_passwords['foo'])
        response = self.c.post(comment.get_update_url(), {
            'rating': new_rating,
            'body': new_body,
        }, follow=True)

        updated_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(comment.pk, updated_comment.pk)
        self.assertEqual(updated_comment.rating, new_rating)
        self.assertEqual(updated_comment.body, new_body)

    def test_comment_editing_validation(self):
        """ Test auth validation for CommentUpdateView """
        product = Product.objects.get()
        user = User.objects.get(username='foo')
        comment = Comment.objects.create(
            user = user,
            product = product,
            rating = 3,
            body = 'Original comment',
        )

        new_rating = 5
        new_body = 'Edited comment'

        self.c.login(username='bar', password=self.raw_passwords['bar'])
        response_wrong_user = self.c.post(comment.get_update_url(), {
            'rating': new_rating,
            'body': new_body,
        }, follow=True)

        updated_comment_1 = Comment.objects.get(pk=comment.pk)

        self.assertEqual(response_wrong_user.status_code, 403)
        self.assertContains(response_wrong_user, '403 Forbidden', status_code=403)
        self.assertContains(response_wrong_user, 
            'No cuentas con los permisos suficientes para editar comentarios de terceros.', 
            status_code=403
        )

        self.assertEqual(updated_comment_1.rating, comment.rating)
        self.assertEqual(updated_comment_1.body, comment.body)

        response_wrong_values = self.c.post(comment.get_update_url(), {
            'rating': 0,
            'body': new_body,
        }, follow=True)