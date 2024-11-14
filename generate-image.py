import openai
import base64

# Step 1: Create a variable api_key and assign a key loaded from file "secrets.txt"
with open("secrets.txt", "r") as file:
    api_key = file.read().strip()

# Step 2: Load file content from data/article.txt to a variable article_text
with open("data/article.txt", "r") as file:
    article_text = file.read()

# Step 3: Add this line: client = OpenAI(api_key=api_key)
client = openai.OpenAI(api_key=api_key)

# Step 4: Call the api by giving the message article_text
response = client.images.generate(
    model = "dall-e-3",
    prompt='Generate an image related to the article below:\n\n' + article_text,
    size="1792x1024",
    response_format="b64_json",
)
# print(response)

# Step 5: Convert base64 to binary
image_data = base64.b64decode(response.data[0].b64_json)

# Step 6: Save the data to image file
with open("generated-files/article-image.png", "wb") as file:
    file.write(image_data)
