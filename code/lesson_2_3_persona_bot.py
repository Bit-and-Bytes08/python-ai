from langchain.chat_models import init_chat_model


"""
Persona Chatbot with Real Facts, Memory, Dynamic Personas,
and Direct Menu Price Lookups.

The chatbot only uses the business facts provided in the facts
dictionary and supports persona switching and conversation memory.
"""


# Why: Keeping business information in one dictionary makes the
# chatbot easy to update without changing the main chatbot logic.
facts = {
    "business_name": "Sweet Crumbs Bakery",
    "location": "Lahore, Pakistan",
    "hours": "9:00 AM to 9:00 PM daily",
    "specialty": "Freshly baked artisan pastries and cakes",
    "prices": {
        "cupcake": 250,
        "brownie": 300,
        "cookie": 150
    }
}


# Different personality styles for the chatbot
personas = {
    "friendly": "friendly and warm, uses simple and cheerful words",
    "sales": "excited, enthusiastic, and always suggests one extra item to buy",
    "formal": "professional, polite, and formal"
}


# Why: Configuration values are kept together so the model and
# memory behavior can be changed easily from one place.
config = {
    "model": "gemma3:1b",
    "temperature": 0.2,
    "memory_size": 8
}


def system_prompt(style):
    """
    Creates the system prompt using the business facts and
    selected persona style.
    """

    return (
        f"You are a helpful AI assistant for {facts['business_name']} "
        f"located in {facts['location']}. "
        f"Hours: {facts['hours']}. "
        f"Specialty: {facts['specialty']}. "
        f"Current menu prices in PKR: {facts['prices']}. "
        f"Adopt this personality style: {style}. "
        f"CRITICAL: You must ONLY use these facts to answer questions. "
        f"If asked about something not in these facts, admit you do not know."
    )


# Initialize the model once
llm = init_chat_model(
    model=config["model"],
    model_provider="ollama",
    temperature=config["temperature"]
)


# Start with the friendly persona
current_persona = personas["friendly"]

messages = [
    {
        "role": "system",
        "content": system_prompt(current_persona)
    }
]


while True:

    user_input = input("You: ").strip()

    if not user_input:
        continue

    # Exit commands
    if user_input.lower() in ("bye", "exit", "stop"):
        print("Bot: Goodbye!")
        break


    # /reset command
    if user_input.lower() == "/reset":
        current_persona = personas["friendly"]

        messages = [
            {
                "role": "system",
                "content": system_prompt(current_persona)
            }
        ]

        print("Bot: Memory has been reset.")
        continue


    # /count command
    if user_input.lower() == "/count":
        print(f"Bot: Messages in memory: {len(messages)}")
        continue


    # Why: Price questions are handled directly from the dictionary
    # so they do not waste an AI call and always return exact prices.
    if user_input.lower().startswith("/price"):

        parts = user_input.split(" ", 1)

        if len(parts) < 2:
            print("Bot: Please provide an item name.")
            continue

        item = parts[1].strip().lower()

        price = facts["prices"].get(item)

        if price is not None:
            print(f"Bot: The price of {item} is PKR {price}.")
        else:
            print(f"Bot: Sorry, {item} is not on our menu.")

        continue


    # Persona command
    if user_input.lower().startswith("/persona"):

        parts = user_input.split(" ", 1)

        if len(parts) < 2:
            print("Bot: Please provide a persona name.")
            print("Available personas: friendly, sales, formal")
            continue

        persona_name = parts[1].strip().lower()

        # Why: .get() gives us a safe default, so an invalid persona
        # never crashes the chatbot.
        selected_persona = personas.get(
            persona_name,
            personas["friendly"]
        )

        current_persona = selected_persona

        # Update the existing system message
        messages[0]["content"] = system_prompt(current_persona)

        if persona_name in personas:
            print(f"Bot: Persona changed to {persona_name}.")
        else:
            print(
                "Bot: Unknown persona. "
                "Using friendly persona instead."
            )

        continue


    # Add user message to conversation memory
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # Send conversation history to the AI
    result = llm.invoke(messages)


    # Add AI response to memory
    messages.append(
        {
            "role": "assistant",
            "content": result.content
        }
    )


    print(f"Bot: {result.content}")


    # Print input tokens if available
    input_tokens = result.usage_metadata.get("input_tokens", 0)
    print(f"Input tokens: {input_tokens}")


    # Why: Limiting memory prevents the conversation history from
    # growing forever while keeping the system instructions.
    if len(messages) > config["memory_size"] + 1:
        messages = [messages[0]] + messages[-config["memory_size"]:]
