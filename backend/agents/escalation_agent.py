from db.db_client import log_conversation
from my_lm_chain import resolve  # import the LM Studio chain from your other file
#from chains.lm_studio_chain import resolve

# Rule-based escalation
def should_escalate(intent: str, sentiment: str, kb_found: bool) -> bool:
    if intent == 'Complaint' and sentiment in ('Angry', 'Frustrated'):
        return True
    if not kb_found:
        return True
    return False

def escalate_and_log(record: dict):
    record['escalated'] = True
    log_conversation(record)
    # In production: push to Zendesk/Freshdesk
    return True

def handle_conversation(record: dict) -> str:
    """
    Decides whether to escalate or answer with LM Studio.
    Logs the conversation in both cases.
    """
    intent = record.get("intent", "")
    sentiment = record.get("sentiment", "")
    kb = record.get("kb", "")
    kb_found = bool(kb.strip())
    user_message = record.get("user_message", "")

    if should_escalate(intent, sentiment, kb_found):
        record['escalated'] = True
        log_conversation(record)
        # In production: push to Zendesk/Freshdesk
        return "Your request has been escalated to a human agent."
    else:
        # Use LM Studio chain to generate reply
        reply = resolve(intent, kb, sentiment, user_message)
        record['reply'] = reply
        record['escalated'] = False
        log_conversation(record)
        return reply
