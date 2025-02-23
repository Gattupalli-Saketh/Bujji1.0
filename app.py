import ollama
import gradio as gr

# Function to interact with the custom llama 2 model
def ask_llama(prompt):
    try:
        response = ollama.generate(model='Bony', prompt=prompt)
        return response['response']
    except Exception as e:
        print(f"An error occurred while generating a response: {e}")
        return "Sorry, I couldn't generate a response. Please try again."

# Function to handle the Gradio interface
def chat_with_llama(query):
    if query.strip().lower() in ["exit", "quit"]:
        return "Goodbye!"
    
    response = ask_llama(query)
    return response

# Create a Gradio interface
iface = gr.Interface(
    fn=chat_with_llama,
    inputs=gr.Textbox(lines=2, placeholder="Type your query here..."),
    outputs="text",
    title="Bujji - Chat with Llama 2",
    description="Type your query and Bujji will respond!"
)

# Launch the Gradio app
iface.launch()