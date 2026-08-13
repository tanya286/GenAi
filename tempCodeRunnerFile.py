from transformers import pipeline

translator= pipeline("translation", model="helsinki-NLP/opus-mt-hi-en")

hindi_text= ["भारत में रूस के ऊर्जा पर निर्भरता बढ़ने के समय में प्रतिबंध बिल आता है",
 "जो पश्चिम एशिया युद्ध के कारण हॉर्मुज की खाड़ी के माध्यम से शिपिंग को बाधित कर रहा है। ",
 "ईरान-यूएस युद्ध ने खाड़ी कच्चे माल की आपूर्ति को रोक दिया है"
 ]

result= translator(hindi_text, max_length=100)

for hi, en in zip(hindi_text, result):
    print(f"Hindi: {hi}\nEnglish: {en['translation_text']}\n")