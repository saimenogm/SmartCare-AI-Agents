import os
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyDniHLv_Bp-MOLiz8vkF_82MpdiID0q_zE"
genai.configure(api_key=GEMINI_API_KEY)

def retrieve(query: str, k: int = 3):
    """Use Gemini to answer questions based on general knowledge"""
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""You are a customer support knowledge base. Answer the following question concisely and accurately:

Question: {query}

Provide a helpful answer based on common customer support scenarios."""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Knowledge base temporarily unavailable: {str(e)}"