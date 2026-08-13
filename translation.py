from transformers import pipeline

translator= pipeline("translation", model="helsinki-NLP/opus-mt-hi-en")

hindi_text= ["रिपब्लिक् ऑफ़् इण्डिया) दक्षिण एशिया में स्थित भारतीय उपमहाद्वीप का सबसे बड़ा देश है",
 " भारत भौगोलिक दृष्टि से विश्व का सातवाँ सबसे बड़ा देश है, जबकि जनसंख्या के दृष्टिकोण से विश्व का सबसे बड़ा देश है ",
    "भारत की राजधानी नई दिल्ली है, जो देश का दूसरा सबसे बड़ा शहर है।",
 ]

result= translator(hindi_text, max_length=100)

for hi, en in zip(hindi_text, result):
    print(f"Hindi: {hi}\nEnglish: {en['translation_text']}\n")