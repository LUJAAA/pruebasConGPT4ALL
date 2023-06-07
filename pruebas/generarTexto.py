import gpt4all
import os
import sys
gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy.bin")
opcion = 0
while opcion == 0:
    os.system("cls")
    print("INGRESE UNA PREGUNTA")
    prompt = str(input())
    os.system("cls")
    # Run model on prompt
    messages = [{"role": "user", "content": prompt}]
    response = gptj.chat_completion(messages)

    print(response)

    print("")
    print("OTRA PREGUNTA 0->SI  1->NO")
    opcion = int(input())

