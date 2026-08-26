from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import  ChatGroq

docs = PyPDFLoader(r"c:\Users\User\Desktop\52485afc-2a5f-4fcb-889d-9fcdc7a5ba8b_SIDH Training Partner Manual RPL Type 3.pdf").load()
chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db= FAISS.from_documents(chunks, embeddings)
question=input('Ask Anything : ')
context_docs=db.similarity_search(question, k=3)
context_text="\n\n".join(doc.page_content for doc in context_docs)
llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0, api_key="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")
response =llm.invoke(f"""Use ONLY this context to answer:
Context:{context_text}
Question:{question} """)
print(response.content)