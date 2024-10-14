import azure.functions as func
from azure.durable_functions import DurableOrchestrationClient
import logging
import json

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = DurableOrchestrationClient(starter)

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON"}),
            status_code=400,
            headers={"Content-Type": "application/json"}
        )
    instance_id = await client.start_new("Orchestrator", None, req_body)
    logging.info(f"Started orchestration with ID = '{instance_id}'.")
    return client.create_check_status_response(req, instance_id)   