import tempfile

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor,DockerCommandLineCodeExecutor

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
# executor = LocalCommandLineCodeExecutor(
#     timeout=10,  # Timeout for each code execution in seconds.
#     work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
# )

# using docker instead of local commandline

executor = DockerCommandLineCodeExecutor(
    image="python:3.12-slim",  # Execute code using the given docker image name.
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration.
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the local command line code executor.
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)

message_with_code_block = """
```python
a=4
print(f"hola como le va {a}")
```
"""

# Generate a reply for the given code.
reply = code_executor_agent.generate_reply(messages=[{"role": "user", "content": message_with_code_block}])
print(reply)