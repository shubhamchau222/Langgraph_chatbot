# LangGraph Chatbot

A modular, multi-threaded chatbot built with [Streamlit](https://streamlit.io/), [LangGraph](https://github.com/langchain-ai/langgraph), and [LangChain](https://github.com/langchain-ai/langchain). This project demonstrates how to build a conversational AI with persistent chat threads, a sidebar for managing conversations, and integration with LLMs.

---

## Features

- **Multi-threaded chat:** Start, switch, and delete chat threads.
- **Persistent conversations:** Chat history is saved and can be reloaded.
- **Sidebar UI:** Manage all your conversations easily.
- **LLM integration:** Uses LangChain and LangGraph for advanced conversational flows.
- **Configurable backend:** Easily switch LLM providers and database backends.

---

## Folder Structure

```
.
└── langgraph_chatbot/
    ├── config/
    │   ├── __init__.py
    │   └── internal.yaml
    ├── core/
    │   ├── nodes.py
    │   ├── state.py
    │   ├── tools.py
    │   └── __init__.py
    ├── graphs/
    │   ├── chatbot_graph.py
    │   └── __init__.py
    ├── utils/
    │   ├── common_utils.py
    │   ├── database_connector.py
    │   ├── llm_utils.py
    │   └── thread_ops.py # not required
    ├── api.py
    ├── streamlit_app.py
    ├── pyproject.toml # your project requirements
    ├── .python-version
    ├── .env
    ├── .gitignore
    ├── chatbot.db #artifact (will create automatically) 
    └── .venv/ #your environment
```

---
## snapshot
![Architecture Diagram](https://github.com/shubhamchau222/Langgraph_chatbot/blob/main/Images/chatbot.png)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langgraph_chatbot.git
cd langgraph_chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

- Copy `.env.example` to `.env` and fill in your API keys and settings.
- Edit `config/internal.yaml` to set your LLM provider and model.

### 5. Run the App

```bash
streamlit run streamlit_app.py
```

---

## Usage

- **Start a new chat:** Click "New Chat" in the sidebar.
- **Switch threads:** Click on any thread ID in the sidebar to load its conversation.
- **Delete a thread:** Click the 🗑️ icon next to a thread to delete it.
- **Chat:** Type your message in the input box and press Enter.

---

## Customization

- **Change LLM provider:** Edit `config/internal.yaml` and update your model/provider.
- **Add new nodes:** Extend `core/nodes.py` and update the graph in `graphs/chatbot_graph.py`.
- **Database backend:** The default uses SQLite via LangGraph's `SqliteSaver`. You can swap this for another backend if needed.

---

## Troubleshooting

- **ModuleNotFoundError:** Ensure all folders have `__init__.py` and use relative imports within packages.
- **Environment variables:** Make sure your `.env` file is set up and loaded.
- **Streamlit issues:** Try clearing the cache with `streamlit cache clear`.

---

## Contributing

Pull requests and issues are welcome! Please open an issue for bugs or feature requests.

---

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Streamlit](https://streamlit.io/)