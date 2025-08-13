from typing import TypedDict, Annotated
import os
import sys

from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from .state import ChatState


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import read_yaml
from core import load_llm

ConfigPath= "./config/internal.yaml"

# Load environment variables
load_dotenv()

def chat_node(state: ChatState):
    """
    A single LangGraph node for handling chat messages.
    """
    llm= load_llm(ModelConfigPath=ConfigPath)
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}


## Testing code
# if __name__ == "__main__":
#     llm = load_llm(ConfigPath)
#     print(llm.invoke("hello world!"))
   