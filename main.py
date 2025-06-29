"""Main"""

#import boto3
from langchain.chat_models import init_chat_model

from langchain_core.messages import HumanMessage

from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph import StateGraph, MessagesState, START

DB_URI = "postgresql://svc_revision_bot:svc_revision_bot@localhost:5432/revision_bot?sslmode=disable"

model_id = "amazon.titan-text-lite-v1"
model = init_chat_model(
    model_id, 
    model_provider="bedrock_converse")

def reconstruct_state_graph():
    pass

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    # checkpointer.setup() - TODO: don't forget to create a setup script

    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}

    config = {
        "configurable": {
            "thread_id": "4"
        }
    }
    
    checkpoints = checkpointer.list(config)
    builder = StateGraph(MessagesState)
    checkpoints = list(checkpointer.list(config, limit=1))
    for checkpoint in checkpoints: 
        print("\nCHECKPOINT")
        print(checkpoint[3]['configurable']['checkpoint_id'])

    """
    for chunk in graph.stream(
        {"messages": [{"role": "user", "content": "hi! I'm bob"}]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1]

    for chunk in graph.stream(
        {"messages": [{"role": "user", "content": "what's my name?"}]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1]

    print(graph.get_graph())
    """

"""
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
    """