from langchain import LLMChain, PromptTemplate
# from langchain.llms import OpenAI      # Uncomment if you're on older LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDniHLv_Bp-MOLiz8vkF_82MpdiID0q_zE"

# Initialize Gemini LLM (choose gemini-1.5-flash or gemini-1.5-pro)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", # Recommended: Use the latest and most stable flash model
    temperature=0.1,
    max_output_tokens=50
)

# Prompt template
prompt = PromptTemplate(
    input_variables=['intent','kb','sentiment','user_message'],
    template=(
        "You are a helpful support assistant. Given the user message, intent, "
        "retrieved knowledge (kb), and sentiment, produce a concise, empathetic, "
        "and actionable reply.\n\n"
        "User message:\n{user_message}\n\n"
        "Intent: {intent}\n\n"
        "Knowledge:\n{kb}\n\n"
        "Sentiment: {sentiment}\n\n"
        "Reply:"
    )
)

# Create LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Function to generate response
def resolve(intent: str, kb: str, sentiment: str, user_message: str) -> str:
    resp = chain.run(intent=intent, kb=kb, sentiment=sentiment, user_message=user_message)
    return resp.strip()
