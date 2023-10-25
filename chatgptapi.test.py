import openai
from senha import API_KEY


openai.api_key = API_KEY

messages = []
#Opicional, teste para comportamento do chatbot (emoção)
# system_msg = input("Que tipo de chatbot você quer criar?\n")
# messages.append({"role": "system", "content": system_msg})

print("Seu novo assistente está pronto! Envie sua primeira mensagem: ")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")