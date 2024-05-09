from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
#from langchain_community.callbacks.tracers.wandb import WandbTracer
import chainlit as cl



DB_FAISS_PATH = "vectorstores/db_faiss"

custom_prompt_template = """Use this following pieces of information to answer the user's question.
If you dont know the answer, please just say that you dont know the answer, and dont try to make up an answer.

Context: {context}
Question: {question}

Only retuen the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    """
    prompt template for QA retrieval for each vector stores
    """

    prompt = PromptTemplate(template=custom_prompt_template, input_variables = ['context','question'])
    return prompt

def load_llm():
    llm = CTransformers(
        model = "C:\\Users\\eashw_i3025bi\\Documents\\MedRag\\llama-2-7b.ggmlv3.q8_0.bin",
        model_type = "llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = db.as_retriever(search_kwargs={'k':2}),
        return_source_documents =True,
        chain_type_kwargs = {'prompt' : prompt}   
        )
    
    return qa_chain

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device':'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings,allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa

def final_result(query):
    qa_result = qa_bot()
    qa_result.update_query(query)
    response = qa_result({'query':query})
    return response

@cl.on_chat_start
async def start():
    chain = qa_bot()
    cl.user_session.set("chain",chain)
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to the medical bot. What is your query?"
    await msg.update()
    
@cl.on_message
async def main(message):
    #message=str(message)
    chain = cl.user_session.get("chain")
    cb =cl.AsyncLangchainCallbackHandler(
        stream_final_answer = True, answer_prefix_tokens = ["FINAL", "ANSWER"]
    )
    cb.answer_reached=True
    res = await chain.acall(str(message.content), callbacks=[cb])
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        answer += f"\nSources:" + str(sources)
    else:
        answer += f"\nNo Sources Found"

    await cl.Message(content=answer).send()