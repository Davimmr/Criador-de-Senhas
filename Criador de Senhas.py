import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0213456789"
symbols = "@#$%&*()_+!{[}]^~;:"

## somar todas as strings
for_pass = lower_case + upper_case + numbers + symbols

tamanho_senha = 15

password = "".join(random.sample(for_pass, tamanho_senha))

print("Utilize esta senha: ", password)