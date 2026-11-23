from promptflow.core import tool


@tool
def format_output(llm_output: str) -> str:
    """Clean up the LLM's answer before it is returned to the user."""
    answer = " ".join(llm_output.split())    # trim and collapse whitespace/newlines
    answer = answer.strip("\"'`").rstrip(".") # drop wrapping quotes and a trailing period
    return f"Solution: {answer}"
