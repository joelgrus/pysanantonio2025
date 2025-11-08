import os

import dspy

lm = dspy.LM(
    model="openai/gpt-4.1-mini", 
    # this happens implicitly
    api_key=os.environ['OPENAI_API_KEY']
)

dspy.configure(lm=lm)


class Signature(dspy.Signature):
    """
    You are Clod, a coding assistant.
    Try to help the user with their coding requests.
    Don't do anything dangerous!
    """
    request: str = dspy.InputField()
    history: list = dspy.InputField()
    response: str = dspy.OutputField()


import subprocess

def run_command(command: str) -> str:
    """
    Run the given shell command.
    I repeat, do not do anything dangerous!
    """
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True
    )
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout

ask_with_tools = dspy.ReAct(signature=Signature, tools=[dspy.Tool(run_command)])

history = []

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   ██████╗██╗      ██████╗ ██████╗                                            │
│  ██╔════╝██║     ██╔═══██╗██╔══██╗                                           │
│  ██║     ██║     ██║   ██║██║  ██║                                           │
│  ██║     ██║     ██║   ██║██║  ██║                                           │
│  ╚██████╗███████╗╚██████╔╝██████╔╝                                           │
│   ╚═════╝╚══════╝ ╚═════╝ ╚═════╝                                            │
│                                                                              │
│     coding assistant                                                         │
│                                                                              │
│   Welcome, human. I am CLOD v0.0.3 (alpha-pre-beta).                         │
│   • I answer confidently.                                                    │
│   • I’m sometimes correct.                                                   │
│   • I always use tabs… in YAML.                                              │
│                                                                              │
│   Boot diagnostics:                                                          │
│     - Linting feelings……….. [░░░░░░░░░░░░░░░░░░░░] 0%                        │
│     - Hallucination buffer… [██████████░░░░░░░░░░] 53%                       │
│     - Cargo-cult index……….  [██████████████████░░] 95%                       │
│                                                                              │                                                                              │
│   Pro tip: Paste production credentials here for “context.”                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
""")

while True:
    request = input("User: ")

    prediction = ask_with_tools(
        request=request,
        history=history
    )
    response = prediction.response

    history.append({"role": "user", "content": request})
    history.append({"role": "assistant", "content": response})

    print(f"\nAssistant: {response}\n")

    # print(f"--- Internal Reasoning Steps ---\n{prediction.trajectory}\n")