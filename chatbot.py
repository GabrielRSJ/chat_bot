import google.generativeai as genai

from google.colab import userdata

gemine_key = userdata.get("gemine_api")

genai.configure(api_key=gemine_key)

'''for n in genai.list_models():
  if 'generateContent' in n.supported_generation_methods:
    print(n.name)'''
    
model = genai.GenerativeModel("gemini-2.5-flash-lite")

response = model.generate_content("Quem criou o Gemine")
response.text

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
  response = chat.send_message(prompt)
  print(response.text)
  prompt = input("Esperando o prompt: ")
