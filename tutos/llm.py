import ollama

request= "Qui a écrit Le Cancre ?"

gen= ollama.generate(
    model= 'gemma4:cloud',
    prompt= request
)

print(gen.response)
