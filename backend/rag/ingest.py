import os
from qdrant_client import QdrantClient
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Qdrant
from langchain.document_loaders import TextLoader


QDRANT_URL = os.environ.get('QDRANT_URL')
QDRANT_API_KEY = os.environ.get('QDRANT_API_KEY')


client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)


emb = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')


def ingest_docs(folder_path: str = './data'):
# Simple ingestion of .txt files in folder
docs = []
import glob
for p in glob.glob(folder_path + '/*.txt'):
loader = TextLoader(p, encoding='utf-8')
docs.extend(loader.load())


qdrant = Qdrant.from_documents(documents=docs, embedding=emb, url=QDRANT_URL, prefer_grpc=False, api_key=QDRANT_API_KEY, collection_name='support_kb')
return qdrant