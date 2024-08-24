from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()


from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever = vector.as_retriever()


retriever.get_relevant_documents("how to upload a dataset")[0]

from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)


tools = [search, retriever_tool]

from langchain import hub

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama

prompt_template = "请给制作 {product} 的公司起个名字,只回答公司名即可"

ollama_llm = Ollama(model="gemma2")
llm_chain = LLMChain(
    llm = ollama_llm,
    prompt = PromptTemplate.from_template(prompt_template)
)
print(llm_chain("给用户的私人股票投资app"))

