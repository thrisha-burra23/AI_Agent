from google import genai
import subprocess

# API Key for Gemini
API_KEY = "Api_key" #replace Api_key it with your gemini api key

# Step 1: Generate a task plan
def generate_task_plan(task_description):
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Create a step-by-step plan for this task: {task_description}"
        )
        return response.text.strip()
    except Exception as error:
        print(f"Error creating task plan: {error}")
        return None

# Step 2: Refine the task plan
def refine_task_plan(task_description, changes):
    try:
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"The task plan needs improvement. Task: {task_description}, Requested Changes: {changes}"
        )
        return response.text.strip()
    except Exception as error:
        print(f"Error refining task plan: {error}")
        return None

# Step 3: Run system commands
def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("Command ran successfully! ✅\nOutput:", result.stdout)
            return True
        else:
            print("Error running the command ❌:\n", result.stderr)
            return False
    except Exception as error:
        print(f"Failed to execute command: {error}")
        return False

# Main Function
def main():
    print("Welcome to the AI Task Assistant!")

    # User input for the task
    task_description = input("What task do you need help with? ")

    # Create and display the task plan
    print("\nGenerating task plan...")
    task_plan = generate_task_plan(task_description)
    if not task_plan:
        print("Could not create a plan. Exiting...")
        return
    print("\nTask Plan:\n", task_plan)

    # User approval
    approval = input("Do you approve this plan? (yes/no): ").lower()
    while approval != "yes":
        changes = input("What changes would you like? ")
        task_plan = refine_task_plan(task_description, changes)
        if not task_plan:
            print("Could not refine the plan. Exiting...")
            return
        print("\nUpdated Task Plan:\n", task_plan)
        approval = input("Do you approve this plan now? (yes/no): ").lower()

    # Command execution
    command = input("Enter the command to run: ")
    success = execute_command(command)

    # If command fails, refine plan and retry
    while not success:
        feedback = input("Task failed. Provide feedback to fix: ")
        task_plan = refine_task_plan(task_description, feedback)
        if not task_plan:
            print("Could not refine the plan. Exiting...")
            return
        print("\nRefined Task Plan:\n", task_plan)
        command = input("Enter the new command to retry: ")
        success = execute_command(command)

    print("Task completed successfully! ✅")

if __name__ == "__main__":
    main()