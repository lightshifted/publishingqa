from langchain.prompts import PromptTemplate
from langchain.memory.motorhead_memory import MotorheadMemory


def create_prompt_template(template: str) -> PromptTemplate:
    return PromptTemplate(
        input_variables=["chat_history", "human_input", "context"],
        template=template
    )

def initialize_memory(
        session_id: str="publishingqa",
        url: str="http://localhost:8080",
        memory_key: str="chat_history",
        input_key: str="human_input",
    ) -> MotorheadMemory:

    return MotorheadMemory(
        session_id=session_id,
        url=url,
        memory_key=memory_key,
        input_key=input_key,
    )