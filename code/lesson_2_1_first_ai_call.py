"""AI Tutor Script for Tuition Centre.

This script prompts the user for a topic and an educational level (beginner or expert),
sends the request to an AI model initialized via langchain's init_chat_model,
and tracks both execution time and token usage for billing/analytical transparency.
"""
from langchain.chat_models import init_chat_model
import time
topic = input("topic: ").strip()
level = input("level (beginner or expert): ")
length = 2

SYSTEM = "You are an expert AI tutor. Explain the following topic to a {level} student in {length} lines."
TEMPERATURE = 0.2
llm = init_chat_model(model="gemma3:1b", model_provider="ollama", temperature = TEMPERATURE )
result = llm.invoke([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": f"explain topic {topic}" }

])

start_time = time.time()
result = llm.invoke([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": f"explain topic {topic}" }

])
end_time = time.time()
elapsed_time = end_time - start_time
token_usage = result.response_metadata.get("token_usage", {})
total_tokens = token_usage.get("total_tokens", "N/A")
print("\n" + "=" * 40)
print(f"--- AI TUTOR RESPONSE ({level.upper()}) ---")
print("=" * 40)
print(result.content)
print("=" * 40)
print(f"Total Tokens Used: {total_tokens}")
print(f"Time Taken: {elapsed_time:.1f} seconds")
print("=" * 40)








