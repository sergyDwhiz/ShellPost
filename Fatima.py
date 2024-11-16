# import requests

# # Replace with your Bing Search API key
# subscription_key = "bc6e9a92e26f4a5ca25148322a3563c5"
# # Replace with your Bing Search API endpoint
# search_url = "https://api.bing.microsoft.com/v7.0/search"

# # Define the search query
# query = "Write an article about Paracetamol P-500 being found to contain the deadly “Mapucho” virus"

# # Set up the headers and parameters for the request
# headers = {"Ocp-Apim-Subscription-Key": subscription_key}
# params = {"q": query, "textDecorations": True, "textFormat": "HTML"}

# # Make the request to the Bing Search API
# response = requests.get(search_url, headers=headers, params=params)
# response.raise_for_status()
# search_results = response.json()


# # Print the search results
# for result in search_results["webPages"]["value"]:
#     print(result["name"])
#     print(result["url"])
#     print(result["snippet"])
#     print()
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

# Path to the model directory
model_path = "path/to/llama_model"

# Load the tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained(model_path)
model = LlamaForCausalLM.from_pretrained(model_path)

# Function to generate text
def generate_text(prompt, max_length=50):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    prompt = "Once upon a time"
    generated_text = generate_text(prompt)
    print("Generated Text:", generated_text)