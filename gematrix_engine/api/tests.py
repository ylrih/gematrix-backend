from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# initialize the APIClient app
client = Client()

class GetTest(TestCase):
    """ Test module """

    def test_me(self):
        # get API response
        response_get = client.get(reverse('get_post_json'))
        response_post = client.post(reverse('get_post_json'))

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_post.status_code, status.HTTP_201_CREATED)



