import logging as lg
from azure.durable_functions import DurableOrchestrationContext, Orchestrator

def orchestrator(context: DurableOrchestrationContext):
    """_summary_
    Args:
        context (Orchestrator): _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    lg.info("Orchestrator function processed a request.")
    req_body = context.get_input()
    outputs = []
    result_activity_hello = yield context.call_activity("Activity_Hello", req_body)
    lg.info(f"Orchestrator received: {result_activity_hello}")
    outputs.append(result_activity_hello)
    return outputs

main = Orchestrator.create(orchestrator)