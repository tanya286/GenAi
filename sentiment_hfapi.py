from huggingface_hub import InferenceClient
client = InferenceClient(token="")
result= client.text_classification(
    "I love xanza course! the faculty is amazing.",
    model="tabularisai/multilingual-sentiment-analysis"

)
print(result)