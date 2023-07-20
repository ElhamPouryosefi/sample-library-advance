from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class BookListAPITest(APITestCase):

    def authenticate(self):
        self.client.post(reverse('register'), {
            "username": "eli",
            "password": "666028",
            "is_author": "True"
        })
        response = self.client.post(reverse('login'), {
            "username": "eli",
            "password": "666028"
        })
        # print(response.data)
        token = response.data['token']
        # print(token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

    def setUp(self):
        self.url = reverse('book')

    def test_get_book_list(self):
        self.authenticate()
        print("---")
        response = self.client.get(self.url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_count_books(self):
    #     self.authenticate()
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.data["count"], 0)

