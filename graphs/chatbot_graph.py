import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from graphs import getDBconnector
from core.nodes import chat_node
from core.state import ChatState

from langgraph.graph import START, END, StateGraph 
from langgraph.checkpoint.sqlite import SqliteSaver

from typing import Any
import logging

##Logger
# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)


#make the connections here

def get_checkpointer() -> SqliteSaver:
    """
    Creates a SqliteSaver checkpointer for LangGraph.

    Returns:
        SqliteSaver: Initialized checkpointer object.
    """
    try:
        conn = getDBconnector()
        checkpointer = SqliteSaver(conn=conn)
        logger.info("Checkpointer initialized successfully.")
        return checkpointer
    except Exception as e:
        logger.exception("Failed to initialize checkpointer.")
        raise e


checkpointer= get_checkpointer()

def create_graph() -> StateGraph:
    """
    Creates and compiles a LangGraph graph with chat_node.

    Returns:
        StateGraph: Compiled LangGraph instance.
    """
    try:
        graph = StateGraph(ChatState)
        graph.add_node("chat_node", chat_node)
        graph.add_edge(START, "chat_node")
        graph.add_edge("chat_node", END)

        chatbot = graph.compile(checkpointer= checkpointer)
        logger.info("Graph compiled successfully.")
        return chatbot
    except Exception as e:
        logger.exception("Failed to create or compile graph.")
        raise e

def retrieve_all_threads(checkpointer=checkpointer):
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)


# if __name__ == "__main__":
#     chatbot_instance = create_graph()
#     logger.info("Chatbot graph is ready.")
