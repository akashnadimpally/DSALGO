import openai
import time

# Set up your API key
openai.api_key = "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"

# Define the prompt you want to use for generating text
prompt = "Hi, I'm ChatGPT. How can I help you today?"

# Define the parameters for the text generation API
model_engine = "text-davinci-002"
max_tokens = 2
temperature = 0.05

# Generate text using the OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature
    )
    time.sleep(50)  # Pause briefly to avoid hitting API rate limits
    return response.choices[0].text.strip()

# Start the conversation with ChatGPT
print(generate_text(prompt))

# Keep the conversation going until the user exits
while True:
    user_input = input("> ")
    prompt += "\nUser: " + user_input + "\nChatGPT:"
    print(generate_text(prompt))
