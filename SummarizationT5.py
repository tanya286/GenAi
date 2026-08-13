from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

long_text = """
The Transformers library by Hugging Face provides a wide range of pre-trained models for natural language processing
tasks. One of the most popular tasks is text summarization, where the goal is to generate a concise summary of a longer piece of text. The T5 model, which stands for Text-to-Text Transfer Transformer, is particularly well-suited for this task. It can take a long input text and produce a shorter version that captures the main points and essential information."""

summary = summarizer(long_text, max_length=50, min_length=25,)
print("Summary:", summary[0]['summary_text'])
