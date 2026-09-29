from hindsight import HindsightEmbedded

memory = HindsightEmbedded(
    profile="incident-response",
    llm_provider="none",
    llm_api_key=""
)

BANK_ID = "incidents"

def remember_incident(text):
    memory.retain(
    bank_id=BANK_ID,
    content=text,
    context="production incident post-mortem",
    document_id=text.split(".")[0]
)


def find_similar_incident(query):
    return memory.recall(
        bank_id=BANK_ID,
        query=query,
        min_scores={"reranker": 0.5}
    )
    