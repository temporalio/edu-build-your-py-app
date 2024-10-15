# Workers are responsible for running your Temporal code. When you start a Workflow in Temporal, tasks get placed into a Task Queue. The Task Queue helps route tasks to the appropriate Worker, which executes the tasks. Workers continuously poll this queue for tasks and execute them. The Workflow doesn't proceed until a Worker picks up and processes the Workflow Task from the Task Queue.

import asyncio

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import say_hello
from workflows import SayHello

async def main():
    # Step 1: Establish a connection with Temporal server.
    client = await Client.connect("localhost:7233", namespace="default")
    # Step 2: Register Workflows and Activities with the Worker.
    # Your Worker is polling the `hello-task-queue` task queue looking for work to be done. 
    worker = Worker(
        client, task_queue="hello-task-queue", workflows=[SayHello], activities=[say_hello]
    )
    # Step 3: Start accepting tasks on the `hello-task-queue` queue
    # The worker runs until it encounters an unexpected error or the process receives a shutdown 
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
