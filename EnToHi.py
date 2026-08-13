from transformers import pipeline

translator= pipeline("translation", model="helsinki-NLP/opus-mt-en-hi")

English_text= ["I agree with you. That sounds like a good idea.",
 " I think you're right about that.",
 "I disagree with your opinion on this matter.",
 ]

result= translator(English_text, max_length=100)

for hi, en in zip(English_text, result):
    print(f"English: {hi}\nHindi: {en['translation_text']}\n")