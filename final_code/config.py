from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

api_key = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY= os.getenv("TAVILY_API_KEY")
from langchain_fireworks import ChatFireworks

from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq


os.environ["FIREWORKS_API_KEY"] = ""

llm = ChatFireworks(model_name="accounts/fireworks/models/deepseek-v3-0324", temperature=0.4, max_retries=2,
                    max_tokens=200)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)

urls = [
    "https://docs.python.org/3/tutorial/index.html",
    "https://realpython.com/python-basics/",
    "https://www.learnpython.org/"
]
