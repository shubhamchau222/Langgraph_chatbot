from .common_utils import read_yaml
from langchain_groq import ChatGroq

def load_llm(ModelConfigPath:str):
    config = read_yaml(ModelConfigPath)

    if not config :
        raise ValueError(f"Could not read YAML configuration from {ModelConfigPath}")
    
    modelSpecs= config['model']['chatmodel']['type']['text-to-text']
    if modelSpecs['api_type'].lower().strip() == 'groq':
        llm= ChatGroq(
            model=modelSpecs['model'],
            temperature=modelSpecs['temperature'],
            max_tokens= modelSpecs['max_tokens']
        )
    return llm