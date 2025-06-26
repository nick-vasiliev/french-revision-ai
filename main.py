"""Main"""

#import boto3
from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage

#client = boto3.client('bedrock')
model_id = "amazon.titan-text-lite-v1"

model = init_chat_model(
    model_id, 
    model_provider="bedrock_converse")

messages=[]

human_message = input("Enter a message: ")
while human_message:
    messages.append(HumanMessage(content=human_message))
    response = model.invoke(messages)
    messages.append(response)
    print(response.content)
    human_message = input("Enter a message: ")