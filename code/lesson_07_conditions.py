"""
Lesson 1.7: Smart Model Router
Demonstrates conditional logic (if/elif/else), input sanitization,
cost calculation, token threshold warnings, and logical operators.
"""

def main():
    # Get and clean task type input
    task_input = input("Task (code / private / chat): ")
    task_type = task_input.strip().lower()

    # Get estimated tokens
    token_input = input("Estimated tokens: ")
    estimated_tokens = int(token_input)

    # Why: Routing tasks to specialized models optimizes both performance and cost efficiency
    if task_type == "code":
        chosen_model = "claude (cloud, strong at code)"
        price_per_1k = 1.5
    elif task_type == "private":
        chosen_model = "llama3.2 (local, Ollama)"
        price_per_1k = 0.0
    else:
        chosen_model = "gpt-4o-mini (cloud, general chat)"
        price_per_1k = 0.25

    # Check token length warning
    if estimated_tokens > 4000:
        print("Warning: long request, consider shortening it.")
    else:
        print("Length is fine.")

    # Calculate cost
    estimated_cost = (estimated_tokens / 1000) * price_per_1k

    # Stretch: Paid vs Free user check for long requests (>2000 tokens)
    is_paid_input = input("Is this a paid user? (yes/no): ").strip().lower()
    if is_paid_input == "no" and estimated_tokens > 2000:
        print("Upgrade to send long requests.")

    print(f"Chosen model: {chosen_model}")
    print(f"Estimated cost: {estimated_cost:.2f} PKR")

if __name__ == "__main__":
    main()