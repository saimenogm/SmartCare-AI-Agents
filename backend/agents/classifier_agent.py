from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDniHLv_Bp-MOLiz8vkF_82MpdiID0q_zE"

# Initialize Gemini LLM (choose gemini-1.5-flash or gemini-1.5-pro)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", # Recommended: Use the latest and most stable flash model
    temperature=0.1,
    max_output_tokens=50
)

# Define prompt
prompt = PromptTemplate(
    input_variables=['text'],
    template='Classify the following customer message into one of: Billing, Technical, Complaint, General.\nMessage:\n{text}\nAnswer with a single word.'
)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt)

# Function
def classify(text: str) -> str:
    resp = chain.run(text=text)
    return resp.strip()
