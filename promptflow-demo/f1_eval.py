from promptflow.core import tool
from azure.ai.evaluation import F1ScoreEvaluator


@tool
def f1_eval(response: str, ground_truth: str) -> float:
    if not ground_truth:          # normal chat, nothing to compare against
        return -1.0
    result = F1ScoreEvaluator()(response=response, ground_truth=ground_truth)
    return result["f1_score"]