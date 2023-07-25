import os
import openai

## openAI API Key
openai.api_key = "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"

def main() :
    print("Processing...")

    ## txt file Load
    with open("Txt/Words.txt") as f :
        words = f.readlines()
    words = [i.strip() for i in words]

    with open("Txt/System.txt", 'r') as f :
        sys_content = f.read()

    request = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : sys_content
            }
        ],
        temperature = 1,
        max_tokens = 256,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    print(request.choices[0].message.content)

if (__name__ == "__main__") :
    main()