# Activities are the building blocks of a Temporal Workflow. They encapsulate the logic for tasks that interact with external services such as querying a database or calling a third-party API. 

# One of the key benefits of using Activities is their built-in fault tolerance. If an Activity fails, Temporal can automatically retry it until it succeeds or reaches a specified retry limit. This ensures that transient issues, like network glitches or temporary service outages, don't result in data loss or incomplete processes.

# To keep things focused on the Workflow logic, these Activities will only contain basic log statements.

from temporalio import activity

@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"
