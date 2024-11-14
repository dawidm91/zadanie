import openai

# Step 1: Create a variable prompt_end
prompt_end = ' . Output the content without comments and additional information, and only plain text without wrapping the code in triple backticks.'

# Step 2: Create a variable api_key and assign a key loaded from file "secrets.txt"
with open("secrets.txt", "r") as file:
    api_key = file.read().strip()

# Step 3: Load file content from prompts/generate-article.txt to prompt_text
with open("prompts/generate-article-v2.txt", "r") as file:
    prompt_text = file.read()

# Step 4: Load file content from data/article.txt to a variable article_text
with open("data/article.txt", "r") as file:
    article_text = file.read()

# Step 5: Add this line: client = OpenAI(api_key=api_key)
client = openai.OpenAI(api_key=api_key)

# Step 6: Call the api by giving the message article_text + prompt_end
final_prompt = prompt_text + prompt_end + "Here is the additional data: \n" + article_text
# print(final_prompt)
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": final_prompt
        }
    ],
    model="gpt-4o-mini",
    seed=12345678
)

# Step 7: Save the response to generated-files/article.html
with open("generated-files/article.html", "w", encoding="UTF-8") as file:
    file.write(response.choices[0].message.content)
