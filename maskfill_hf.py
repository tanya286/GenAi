from huggingface_hub import InferenceClient
client = InferenceClient(token="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")
result= client.fill_mask(
    "i love to play [MASK] in the evening.",
    model="distilbert/distilbert-base-uncased",
 
)   
print(result[0])