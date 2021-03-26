import os
import openai

# Max tokens 6
# Temperaturee 0
# Top p 1.0
# Frequency penalty 0.0
# Presence penalty 0.0
# Stop sequence \n

print("hello world")

# 1. create a user prompt
# 2. Parse userprompt into GPT3 classifier
# 3. Parse again using sub classifiers

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Completion.create(
  engine="davinci",
  prompt="""The following is a list of companies and the categories they fall into\n\n
  Facebook: Social media, Technology\n
  LinkedIn: Social media, Technology, Enterprise, Careers\n
  Uber: Transportation, Technology, Marketplace\n
  Unilever: Conglomerate, Consumer Goods\n
  Mcdonalds: Food, Fast Food, Logistics, Restaurants\n
  FedEx:""",
  temperature=0,
  max_tokens=6,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)
