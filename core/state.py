from typing import TypedDict, Annotated
from langgraph.graph.message import BaseMessage, add_messages

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]