import os
import sys
from openai import OpenAI

prompt_end = ' . Output the content without comments and additional information, and only plain text without wrapping the code in triple backticks.'

with open("secrets.txt", "r") as file:
    api_key = file.read().strip()

client = OpenAI(
    api_key=api_key
)

def call(message):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-4o-mini",
        seed=12345678
    )
    # print(response)
    return response.choices[0].message.content

def read_file(path):
    with open(path, 'r') as file:
        content = file.read()
        # print(content)
        return content

def write_to_file(path, content):
    with open(path, 'w', encoding="UTF-8") as file:
        file.write(content)    

if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Usage: python script.py <input-filename> <output-filename> <optional-input-data>")
    else:
        prompt = read_file(os.path.join('prompts', sys.argv[1]))
        prompt += prompt_end
        if (len(sys.argv) == 4 and sys.argv[3]):
            data = read_file(os.path.join('data', sys.argv[3]))
            prompt += "Here is the additional data: \n" + data
        # print('prompt', prompt)
        response = call(prompt)
        write_to_file(os.path.join('generated-files', sys.argv[2]), response)
