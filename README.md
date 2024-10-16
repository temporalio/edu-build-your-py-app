# Build Your Own Temporal Application in Python!

You are going to build your own Temporal application in Python! But first, as a prerequisite, let's run through a simple application that prints "Hello, Temporal!". Follow the steps below to run the _Hello World_ sample.

## Using the Exercise Environment

We want to minimize the barriers for learning Temporal, and we know that not everyone is able or willing to install software on their computers for a training course. That's why we use the GitPod service to provide a browser-based exercise environment for you to use.

The only thing you'll need besides an up-to-date Web browser is a GitHub account that you can log into from that browser, which allows the GitPod service to set up the exercise code you'll use during the course.

Launch the exercise environment [here](https://gitpod.io/new/#https://github.com/temporalio/edu-build-your-py-app).

## How to Navigate to Your Files

Before you begin, you need to know how to navigate to certain files using git.    
- **Listing Files in a Directory**: In your terminal window, enter `ls` to list the contents of the current folder that you are in. Go ahead and try it now! You should see the directory files listed such as `README.md`, `hello-world`, `create-your-app`.
- **Entering a Folder**: To go into a folder, type `cd` followed by the folder name. For example, if you do `cd hello-world`, you will now enter the `hello-world` folder.   
    - Try it now and you will see that you have entered the `hello-world` directory. 
    - Type `ls` again to list all the files in your `hello-world` folder.
- **Going Backwards**: Enter `cd ..` to navigate back out to the previous directory. Try it now, and you will see you are back in the root directory.

## Hello World Sample:

### Setup: If you're using the Gitpod environment to run this exercise, you can skip these steps.

1. For the exercises, make sure to run `temporal server start-dev --ui-port 8080 --db-filename clusterdata.db` in one terminal window to start the Temporal server.  
2. Add another terminal window in addition the one running the Temporal server. You can do this by right clicking a terminal window and click `New Terminal`. 
3. All Python libraries for this course should be installed in a virtual environment. If you are running these exercises in the course's GitPod environment, there is a virtual environment already setup for you and you can skip this section. If you are running these exercises locally, be sure you are using Python 3.7+. 
    1. Run the following command to create a virtual environment: `python3 -m venv env`.
    2. Activate the virtual environment: 
        - Linux/Mac: `source env/bin/activate`
        - Windows: `env/Scripts/activate`
    Once the environment is active you should see (env) prepended to your prompt similar to below: `(env) $`
    3. Install the Temporal SDK: `python -m pip install temporalio`.
For every new terminal you open, you will need to activate the environment using the following command:
        - Linux/Mac: `source env/bin/activate`
        - Windows: `env/Scripts/activate`

### Run a Worker 

1. Navigate into the `hello-world` directory.
2. Now, you will start a Temporal Worker. In a terminal window separate from running the server if you have one running, run `python run_worker.py` to start the Worker.
    - Workers are responsible for running your Temporal code. When you start a Workflow in Temporal, tasks get placed into a Task Queue. The Task Queue helps route tasks to the appropriate Worker, which executes the tasks. Workers continuously poll this queue for tasks and execute them. The Workflow doesn't proceed until a Worker picks up and processes the Workflow Task from the Task Queue.

### Run a Workflow

1. Now, you will run a Workflow. You will need to do this in a separate terminal window. To add more terminal windows in Gitpod, right click a terminal window and click `New Terminal`.
2. To run the Workflow, run `python client.py`.
    - In the terminal window, you should see: `Hello, Temporal!`.
    - A Workflow is a sequence of steps defined by writing code, known as a Workflow Definition. These steps are executed as a Workflow Execution. A Workflow Definition is essentially a function, which can store state and orchestrates the execution of Activities. Workflows manage the coordination and logic of your application's processes, while Activities perform the tasks which interact with external services. As mentioned, the Workflow will orchestrate the sequence of Activities such as sending welcome emails, charging customers, and handling cancellations.
    - Activities are the building blocks of a Temporal Workflow. They encapsulate the logic for tasks that interact with external services such as querying a database or calling a third-party API. One of the key benefits of using Activities is their built-in fault tolerance. If an Activity fails, Temporal can automatically retry it until it succeeds or reaches a specified retry limit. This ensures that transient issues, like network glitches or temporary service outages, don't result in data loss or incomplete processes.

Now that you've run a basic `hello world` application, it's time for you to try creating your own application.

## Create Your Own Application 

### Setup

1. Kill the Worker from the `hello-world` project. In the terminal window where your Worker is running, do `CTRL C`, right click the terminal window, and click `Kill Terminal`. This terminal window will now be removed.
2. In the terminal window where your `hello world` Workflow was running, navigate into the `create-your-app` folder where some boiler code is already provided for you to get started.
    - Enter `cd ..` to navigate back out to the parent directory. You should now be back in the root directory.
    - Enter `ls` to see all the directories. You should see a `create-your-app` directory.
    - Enter the `create-your-app` directory by entering `cd create-your-app`.
3. Start a Temporal Worker that will listen for any work that needs to be performed by running `python run_worker.py` in the same terminal window.
5. Now open a new terminal window where you will run your workflow with `python client.py` once you've created your own workflow.

Have fun building!
