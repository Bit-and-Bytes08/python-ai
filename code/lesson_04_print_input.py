"""Business Prompt Builder
-----------------------
This script automates the creation of tailored AI prompts for a digital agency.
It collects specific business diagnostics from a client and generates a structured
prompt optimized for Large Language Models (LLMs) to provide relevant solutions."""

print(__doc__)
# personal information 
user_name = input("Your name: ")
business_type = input("Business type: ")
biggest_problem = input("Biggest problem: ")

# budget and conversion
budget_input = input("Monthly budget in PKR: ")
budget_pkr = int(budget_input)

print(f"Welcome, {user_name}!")
print("\n--- Your AI Prompt ---")

# ai prompt
ai_prompt = (
    f"Suggest 3 AI solutions for a {business_type} that struggles with {biggest_problem}.\n"
    f"Budget: {budget_pkr:,} PKR per month."
)
print(ai_prompt)
