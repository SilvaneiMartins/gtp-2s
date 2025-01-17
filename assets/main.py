import tiktoken
import safetensors
import torch

# f = open("tiny.txt", "r")
# enc = tiktoken.encoding_for_model("gpt2")
# tokens = enc.encode(f.read())
# text = enc.decode(tokens)

# print(text)

f = open("model.safetensors", "rb")
fts = safetensors.deserialize(f.read())
params = dict()

for ft in fts:
    name = ft[0]
    data = ft[1]["data"]
    shape = ft[1]["shape"]

    params[name] = torch.frombuffer(data, dtype=torch.float32).reshape(shape)


print(params["wte.weight"].shape)

