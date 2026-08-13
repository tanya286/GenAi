from transformers import pipeline

translator= pipeline("translation", model="helsinki-NLP/opus-mt-hi-en")

text= input("Enter the text to be translated from Hindi to English: ")
hindi_text= text.split('।')
result= translator(hindi_text, max_length=100)
for hi, en in zip(hindi_text, result):
    print(f"Hindi: {hi}\nEnglish: {en['translation_text']}\n")