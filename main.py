"""Main"""

#import boto3
from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage

#client = boto3.client('bedrock')
model_id = "amazon.titan-text-lite-v1"

model = init_chat_model(
    model_id, 
    model_provider="bedrock_converse")

messages = [
    #SystemMessage("Translate the following from English into French"),
    HumanMessage("hi!"),
]

response = model.invoke(messages)
print(response)