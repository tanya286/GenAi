from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import  ChatGroq

# 1. Load the PDF document
docs = PyPDFLoader(r"c:\Users\User\Desktop\gate\cd.pdf").load()

# 2. Split the document into smaller text chunks
chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

# 3. Initialize the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Create the FAISS vector database from the text chunks
db = FAISS.from_documents(chunks, embeddings)

# 5. Get user input for the query
question = input('Ask Anything : ')
