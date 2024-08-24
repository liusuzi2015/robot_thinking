from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import Weaviate
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from weaviate.embedded import EmbeddedOptions
import requests
import weaviate

loader = TextLoader('README.md')
documents = loader.load()

# Document segmentation
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

client = weaviate.Client(
  url = "http://localhost:8080"
)
#V4 client connection, which didn't work here.
#client = weaviate.connect_to_local()
print("started doc embedding")
vectorstore = Weaviate.from_documents(
    client=client,
    documents=chunks,
    embedding=OllamaEmbeddings(model="llama3"),
    by_text=False
)

# Retrive part
retriever = vectorstore.as_retriever()
# LLM prompt template
template = """You are an assistant for question-answering tasks.
   Use the following pieces of retrieved context to answer the question.
   If you don't know the answer, just say that you don't know.
   Use three sentences maximum and keep the answer concise.
   Question: {question}
   Context: {context}
   Answer:
   """
prompt = ChatPromptTemplate.from_template(template)

llm = ChatOllama(model="llama3", temperature=10)
rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)
query = "## 贡献中描述了什么?"
print(rag_chain.invoke(query))