from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url=reverse('register/')
        self.register_url=reverse('login/')

        self.user_data={
            'username':"Developer",
            'password':"Thrill@&oo0012",
            'first_name':"Python",
            'last_name':"Django",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()

