# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch
# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True, torch_dtype=torch.bfloat16).cuda()
# input_text = "#write a quick sort algorithm"
# inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
# outputs = model.generate(**inputs, max_length=128)
# print(tokenizer.decode(outputs[0], skip_special_tokens=True))


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# 设置设备为 CUDA（如果可用），否则使用 CPU
device = torch.device("mps" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-6.7b-base", trust_remote_code=True, torch_dtype=torch.bfloat16).to(device)
input_text = "#write a quick sort algorithm"
inputs = tokenizer(input_text, return_tensors="pt").to(device)
outputs = model.generate(**inputs, max_length=128)
decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)