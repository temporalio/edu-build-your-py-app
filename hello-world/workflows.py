# A Workflow is a sequence of steps defined by writing code, known as a Workflow Definition. These steps are executed as a Workflow Execution.
# A Workflow Definition is essentially a function, which can store state and orchestrates the execution of Activities. Workflows manage the coordination and logic of your application's processes, while Activities perform the tasks which interact with external services.
# As mentioned, the Workflow will orchestrate the sequence of Activities such as sending welcome emails, charging customers, and handling cancellations.

from datetime import timedelta
from temporalio import workflow

# Import say_hello activity from activities.py
with workflow.unsafe.imports_passed_through():
    from activities import say_hello

# A workflow that simply calls an activity
@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=5)
        )
