from transformers import AutoTokenizer, AutoModelForCausalLM

# Access token here
huggingface_token = "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"

tokenizer = AutoTokenizer.from_pretrained("google/gemma-7b-it", use_auth_token=huggingface_token)
model = AutoModelForCausalLM.from_pretrained("google/gemma-7b-it", use_auth_token=huggingface_token)

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))