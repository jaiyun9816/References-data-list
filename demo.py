import openai
import json

API_KEY = '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'
openai.api_key = API_KEY

model_id = 'gpt-3-32k'

def chatgpt_conversation(conversation_Log) :
    response = openai.ChatCompletion.create(
        model = model_id,
        messages = conversation_Log
    )
    #print(response)
    conversation_Log.append({
        'role' : response.choices[0].message.role, 
        'content' : response.choices[0].message.content.strip()
    })
    return conversation_Log

f = open('./PDF/img_sample1.pdf', "r")
content = f.read()
conversations = []
conversations.append({'role' : 'user', "content" : content})

conversations = chatgpt_conversation(conversations)
print(conversations[1]['content'])
