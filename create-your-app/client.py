# A Temporal Client is a component available in each Temporal SDK that provides a set of APIs to communicate with a Temporal Service. A Temporal Client is used to start a Workflow, send data to a Workflow, and more. It enables you to perform various operations such as:

# - Start a business process.
# - Get the result of a business process.
# - List business processes or entities.
# - Query the state of your business process.
# - Send data into a running business process.

import asyncio

from workflows import SayHello
from temporalio.client import Client


async def main():
    # Connect to the default Server location
    client = await Client.connect("localhost:7233")

    #  We are executing the `SayHello` Workflow
    # We are placing the `SayHello` Workflow to the `hello-task-queue` task queue. We have a Worker configured to poll for tasks on the `hello-task-queue` task-queue in `run_worker.py`.
    # `Temporal` will be the argument provided to the `SayHello` Workflow.
    result = await client.execute_workflow(
        SayHello.run, "Temporal", id="hello-workflow", task_queue="hello-task-queue"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
