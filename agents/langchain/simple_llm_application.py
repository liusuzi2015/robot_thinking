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
# print(llm_chain.run("袜子"))    # 加个.run也可
