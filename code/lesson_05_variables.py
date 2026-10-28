model_name = "llama3.2"  # type: str
context_window = 128000  # type: int
price_per_1k_tokens = 0.5  # type: float example price in PKR
runs_locally = True  # type: bool
# Why: Displaying the data types alongside values verifies that type inference worked correctly
print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")
user_tokens_input = input("Tokens per chat: ")
tokens_per_chat = int(user_tokens_input)

 # Why: Calculating cost dynamically based on user input demonstrates practical variable usage
estimated_cost = (tokens_per_chat / 1000) * price_per_1k_tokens
rounded_cost = round(estimated_cost, 2)
print(f"Estimated cost: {rounded_cost} PKR")

 # Stretch: Chats per day and monthly cost estimation (30 days)
chats_per_day_input = input("Chats per day (stretch): ")
chats_per_day = int(chats_per_day_input)
monthly_cost = rounded_cost * chats_per_day * 30
print(f"Estimated monthly cost (30 days): {round(monthly_cost, 2)} PKR")
