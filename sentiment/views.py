import os

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view, inline_serializer
from rest_framework.views import APIView
from rest_framework import status, serializers
from transformers import pipeline

from .extended_schema import sentimentAnalyseResponseSchema

from transformers import logging

logging.set_verbosity_warning()  # Disabling some warning messages


# Define the view and extend the schema for POST method on swagger doc
@extend_schema_view(
    post=extend_schema(
        request=inline_serializer(
            name="SentimentAnalyseSerializer", fields={"text": serializers.CharField()}
        ),
        responses={**sentimentAnalyseResponseSchema}  # The output schema
    )
)
class AnalyseSentimentAPIView(APIView):
    """
    Analyse sentiment of a given text

    This API endpoint analyzes the sentiment of a given text. It expects a POST request
    with the 'text' field in the request body. The response contains the sentiment analysis result.
    """

    permission_classes = [AllowAny]  # The API does not require authentication

    def post(self, request, *args, **kwargs):
        text = request.data.get('text', '').strip()

        # Check if the 'text' field is empty and return a 400 status if empty
        if not text:
            return Response(
                data={'message': 'Please send some data!!!'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            model_path = "./model/twitter-roberta-base-sentiment-latest"

            # Check if the model path exists and raise error if doesn't exist
            if not os.path.exists(model_path):
                raise FileNotFoundError("Directory Doesn't exist!!!")

            # Create a sentiment analysis pipeline using the specified model path
            sentiment_pipeline = pipeline(task="sentiment-analysis", model=model_path)

            # Perform sentiment analysis on the text and return 200 response
            sentiment = sentiment_pipeline(text)

            return Response(
                data={'sentiment': sentiment[0]['label']}, status=status.HTTP_200_OK
            )

        except Exception as ex:
            return Response(
                data=str(ex), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
