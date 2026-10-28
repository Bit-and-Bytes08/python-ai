from langchain.chat_models import init_chat_model


def main():
    """
    Chatbot with short-term conversation memory.

    The chatbot keeps the system message and the last 8
    conversation messages. It also supports reset and count commands.
    """

    SYSTEM = (
        "You are a helpful AI assistant. "
        "Answer clearly and briefly."
    )

    TEMPERATURE = 0.2

    # Why: We need the system message to remain in memory permanently.
    messages = [
        {"role": "system", "content": SYSTEM}
    ]

    # Why: Initializing the model once avoids creating a new model
    # connection every time the user sends a message.
    llm = init_chat_model(
        model="gemma3:1b",
        model_provider="ollama",
        temperature=TEMPERATURE,
        max_tokens=200
    )

    while True:
        user_input = input("User: ").strip()

        if user_input.lower() in ("bye", "/exit", "exit", "stop"):
            print("Chatbot: Goodbye!")
            break

        # Why: /reset should remove old conversation context
        # while keeping the system instructions.
        if user_input.lower() == "/reset":
            messages = [
                {"role": "system", "content": SYSTEM}
            ]
            print("Chatbot: Memory reset.")
            continue

        if user_input.lower() == "/count":
            print(f"Messages in memory: {len(messages)}")
            continue

        # Add user's message to memory
        messages.append({
            "role": "user",
            "content": user_input
        })

        # Send the complete conversation history to the model
        result = llm.invoke(messages)

        # Add AI response to memory
        messages.append({
            "role": "assistant",
            "content": result.content
        })
        print(len(messages))
        print(f"Chatbot: {result.content}")

        # Print input tokens used for this request
        input_tokens = result.usage_metadata.get("input_tokens", 0)
        print(f"Input tokens: {input_tokens}")

        # Keep system message + last 8 conversation messages
        if len(messages) > 9:
            messages = [messages[0]] + messages[-8:]


if __name__ == "__main__":
    main()