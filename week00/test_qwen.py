import torch #pytorch 深度学习框架，所有神经网络在这上面跑
from modelscope import snapshot_download #ModelScope 阿里模型社区下载Qwen
from transformers import AutoModelForCausalLM, AutoTokenizer  ##导入库 transformers Hugging Face出的库

model_id = "Qwen/Qwen2.5-0.5B-Instruct"     #
model_dir = snapshot_download(model_id)

tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir, torch_dtype=torch.float16, device_map="auto", trust_remote_code=True
)

messages = [{"role": "user", "content": "你好，用一句话介绍你自己"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

out = model.generate(**inputs, max_new_tokens=80, do_sample=False)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))