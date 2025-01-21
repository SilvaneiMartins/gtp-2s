import tiktoken
import safetensors
import torch
from torch.nn import functional as F

f = open("tiny.txt", "r")
enc = tiktoken.encoding_for_model("gpt2")
tokens = enc.encode(f.read())
# text = enc.decode(tokens)

x = tokens[:64]
y_true = tokens[1:65]

print(x)
print(y_true)
exit(0)

f = open("model.safetensors", "rb") 
fts = safetensors.deserialize(f.read())
params = dict()
for ft in fts:
    name = ft[0]
    data = ft[1]["data"]
    shape = ft[1]["shape"]
    params[name] = torch.frombuffer(data, dtype=torch.float32).reshape(shape)
# print(params["wte.weight"].shape)

F.embedding(input, weight)