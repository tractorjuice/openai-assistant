

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# A Thread represents a conversation. We recommend creating one Thread per user as soon as the user initiates the conversation. Pass any user-specific context and files in this thread by creating Messages.
thread = client.beta.threads.create()

# A Message contains the user's text, and optionally, any files that the user uploads. Image files aren't supported today, but we plan to add support for them in the coming months.
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# You can optionally pass additional instructions to the Assistant while creating the Run:
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

# This creates a Run in a queued status. You can periodically retrieve the Run to check on its status to see if it has moved to completed.
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)

# Once the Run completes, you can retrieve the Messages added by the Assistant to the Thread.
messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

