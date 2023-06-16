from django.urls import reverse
from rest_framework.test import APITestCase


class AnalyseSentimentAPITest(APITestCase):
    # Define the API endpoint URL
    url = reverse('sentiment:analyze')

    def test_analyse_sentiment_with_valid_text(self):
        # Create a payload with valid text
        payload = {'text': 'This is a positive statement.'}

        # Make a POST request to the API
        response = self.client.post(self.url, payload, format='json')

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert that the response contains the expected sentiment key
        self.assertIn('sentiment', response.data)
        sentiment = response.data['sentiment']

        # Assert that the sentiment is one of the expected labels
        self.assertIn(sentiment, ['positive', 'negative', 'neutral'])

    def test_analyse_sentiment_with_empty_text(self):
        payload = {'text': ''}

        # Make a POST request to the API
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, 400)

        # Assert that the response contains the expected error message
        self.assertIn('Please send some data!!!', response.data['message'])

    # Add more test cases as needed for different scenarios
