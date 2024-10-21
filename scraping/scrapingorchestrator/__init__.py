import logging
import json
from azure.durable_functions import DurableOrchestrationContext, Orchestrator
import azure.durable_functions as df

def orchestrator_function(context: df.DurableOrchestrationContext):
    # Retrieve the input data, which is expected to be a JSON object
    func = context.get_input()

    # Check if the input has the required fields
    if not func or 'name' not in func or 'param' not in func:
        logging.error("Invalid input; expected a JSON object with 'name' and 'param'.")
        return "Invalid input"

    # Call the specified activity function with its parameters
    result = yield context.call_activity(func['name'], func['param'])

    # Return only the output value from the result
    return result  # Assuming 'result' contains the output value directly

# Create the orchestrator
main = Orchestrator.create(orchestrator_function)