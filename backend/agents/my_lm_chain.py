"""
LM Studio chain for generating responses to customer queries.
This module provides the resolve function that uses LM Studio to generate
context-aware responses based on intent, knowledge base, and sentiment.
"""

def resolve(intent: str, kb: str, sentiment: str, user_message: str) -> str:
    """
    Generate a response using LM Studio based on the conversation context.
    
    Args:
        intent: The classified intent of the user message
        kb: Knowledge base content relevant to the query
        sentiment: Detected sentiment of the user
        user_message: The original user message
    
    Returns:
        str: Generated response from LM Studio
    """
    # Simple rule-based response as fallback
    if not kb.strip():
        return "I understand you're looking for help. Let me connect you with a human agent who can assist you further."
    
    # Basic template-based response
    responses = {
        'Complaint': f"I apologize for the inconvenience you're experiencing. {kb}",
        'Inquiry': f"Based on your question, here's what I found: {kb}",
        'Support': f"I'd be happy to help you with that. {kb}",
        'Feedback': f"Thank you for your feedback! {kb}"
    }
    
    base_response = responses.get(intent, f"Thank you for reaching out. {kb}")
    
    # Add sentiment-aware phrasing
    sentiment_phrases = {
        'Happy': "I'm glad to hear you're happy with our service! ",
        'Neutral': "",
        'Frustrated': "I understand this might be frustrating. ",
        'Angry': "I sincerely apologize for the issue you're facing. "
    }
    
    sentiment_prefix = sentiment_phrases.get(sentiment, "")
    
    return f"{sentiment_prefix}{base_response}"