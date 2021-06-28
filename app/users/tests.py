from django.test import TestCase, Client, override_settings
from django.contrib import auth
from .models import User
from stores.models import City

# Create your tests here.
@override_settings(PASSWORD_HASHERS=['django.contrib.auth.hashers.SHA1PasswordHasher',])
class UsersTestCase(TestCase):
    def print_user(self, user):
        print(f"Username: {user.username}")
        print(f"Email: {user.email}")
        print(f"Password: {user.password}")
        if user.city is not None:
            print(f"City: {user.city.pk} - {user.city}")
        else:
            print('City: None')
        print(f"In mailing list: {user.in_mailing_list}")
        print()

    def setUp(self):
        self.client = Client()
        
        # City objects
        self.test_cities = []
        self.test_cities.append(City.objects.create(name='Torreón'))
        self.test_cities.append(City.objects.create(name='Gómez Palacio'))
        self.test_cities.append(City.objects.create(name='Lerdo'))
        
        # Test User objects
        self.raw_users = { 
            'foo': ('foo16130789', self.test_cities[0], False),
            'bar': ('bar16130789', None, True),
            #'my_new_user': ('my_secret16130789', self.test_cities)
        }

        self.test_users = {}
        
        def add_test_user(name, data):
            self.test_users[name] = User.objects.create_user(
                username = name,
                email = f"{name}@test_mail.com",
                password = data[0],
                city = data[1],
                in_mailing_list = data[2],
            )

        for key, value in self.raw_users.items():
            add_test_user(key, value)

        #for i in self.test_users.values():
        #    self.print_user(i)
    
    def test_login_view(self):
        """Test if the login template is rendered"""
        
        self.client.logout()
        response = self.client.get('/users/login/', follow=True)        

        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_redirection(self):
        """Test if the login redirects active sessions to the home page"""
        
        self.client.login(username='foo', password=self.raw_users['foo'][0])
        response = self.client.get('/users/login/', follow=True)

        self.assertTemplateNotUsed(response, 'registration/login.html')
        self.assertRedirects(response, '/')

    def test_correct_login(self):
        """Test if the login view logs users in"""
        
        response = self.client.post('/users/login/', {
            'username': 'foo',
            'password': self.raw_users['foo'][0],
        }, follow=True)

        self.assertRedirects(response, '/')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'], self.test_users['foo'])

    def test_incorrect_login(self):
        """Test is the login prevents incorrect credentials to log in"""

        response = self.client.post('/users/login/', {
            'username': 'foo',
            'password': 'wrong_password',
        }, follow=True)

        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTrue(response.context['form'].errors)

    def test_signup_forbidden(self):
        self.client.login(username='foo', password=self.raw_users['foo'][0])

        response_get = self.client.get('/users/signup/', follow=True)
        self.assertEqual(response_get.status_code, 403)

        response_post = self.client.post('/users/signup/', {
            'username': 'my_new_user',
            'email': 'my_new_user@mail.com',
            'password1': 'my_secret16130789',
            'password2': 'my_secret16130789',
        }, follow=True)
        self.assertEqual(response_post.status_code, 403)
    
    def test_user_creation(self):
        # Logout user before signup
        self.client.logout()

        # Send POST request with user data
        new_user_name = 'my_new_user'
        new_user_password = 'my_secret16130789'

        response = self.client.post('/users/signup/', {
            'username': new_user_name,
            'email': f"{new_user_name}@mail.com",
            'password1': new_user_password,
            'password2': new_user_password,
        }, follow=True)

        # Check if redirected to login view after creating the user
        self.assertRedirects(response, '/users/login/')
        
        # Check if new user can be logged in
        self.client.login(username=new_user_name, password=new_user_password)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_changeform_redirect(self):
        self.client.logout()

        response_get = self.client.get('/users/edit/', follow=True)
        self.assertRedirects(response_get, '/users/login/?next=/users/edit/')

        response_post = self.client.post('/users/edit/', {
            'username': 'my_user',
            'email': 'my_new_mail@mail.com',
            'city': '',
        }, follow=True)
        self.assertRedirects(response_post, '/users/login/?next=/users/edit/')

    def test_user_changeform(self):
        self.client.login(username='foo', password=self.raw_users['foo'][0])

        new_mail_1 = 'my_new_mail@mail.com'
        new_city_1 = ''
        new_iml_1 = 'True'

        response_foo = self.client.post('/users/edit/', {
            'username': 'foo',
            'email': new_mail_1,
            'city': new_city_1,
            'in_mailing_list': new_iml_1,
        }, follow=True)

        self.print_user(response_foo.context['user'])

        self.assertEqual(response_foo.context['user'], self.test_users['foo'])
        self.assertEqual(response_foo.context['user'].email, new_mail_1)
        self.assertIsNone(response_foo.context['user'].city)
        self.assertTrue(response_foo.context['user'].in_mailing_list)