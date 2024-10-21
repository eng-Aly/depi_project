from azure.functions import HttpRequest, HttpResponse
from azure.durable_functions import DurableOrchestrationClient
 
 
async def main(req: HttpRequest, starter: str) -> HttpResponse:
    client = DurableOrchestrationClient(starter)
    # instance_id = await client.start_new(req.route_params["functionName"], None, None)
    try:
        req_data = req.get_json()
    except: req_data = dict(req.params)
 
    func = {'name': req.route_params["functionName"], 'param': req_data}
    instance_id = await client.start_new('scrapingorchestrator', None, func)
 
    logging.info(f"Started orchestration with ID = '{instance_id}'.")
 
    return client.create_check_status_response(req, instance_id)