sentimentAnalyseResponseSchema = {
    200: {
        "example": {"sentiment": "positive/negative/neutral"},
    },
    400: {
        "example": {"message": "Please send some data!!!"},
    },
    500: {
        "type": "object",
        "properties": {"message": {"type": "string"}},
    },
}