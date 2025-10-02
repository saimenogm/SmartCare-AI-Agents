from langchain import LLMChain, PromptTemplate
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
    input_variables=['text'],
    template=(
        "Label the sentiment of the following message as one of: "
        "Angry, Frustrated, Neutral, Happy.\n"
        "Message:\n{text}\n"
        "Answer with a single word."
    )
)

# LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

def predict_sentiment(text: str) -> str:
    resp = chain.run(text=text)
    return resp.strip()
