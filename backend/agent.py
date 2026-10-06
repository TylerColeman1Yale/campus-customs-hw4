from pathlib import Path
try:
    from .tools import find_answer
except ImportError:
    from tools import find_answer

PROMPT = (Path(__file__).parent / 'prompts' / 'prompt.md').read_text()

def run_agent(message, product_id=None, user=None):
    # The deterministic database tools provide factual commerce answers. If the
    # optional PydanticAI/OpenAI dependency is configured, this remains the safe
    # tool-backed seam where a model can be added without changing the API.
    return find_answer(message, product_id)
