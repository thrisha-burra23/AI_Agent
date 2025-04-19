
# AI Task Assistant

## Overview

The **AI Task Assistant** is a Python-based program that utilizes Google's Gemini API to automate and simplify tasks on your local computer. By interacting with the user through a command-line interface, the assistant can:
- Generate detailed step-by-step task plans using AI.
- Refine task plans based on user feedback.
- Execute system commands locally.
- Retry failed tasks with refined plans and new commands.

This program is ideal for automating repetitive tasks, executing commands, and providing AI-driven solutions.

---

## Features

1. **Generate Task Plans**:
   - Creates step-by-step task plans using the Gemini API.
   - Helps users visualize and execute tasks efficiently.

2. **Refine Plans**:
   - Accepts feedback for improvement and generates refined plans dynamically.

3. **Command Execution**:
   - Executes system commands provided by the user (e.g., running scripts or compiling programs).

4. **Error Handling and Retry**:
   - Captures and handles errors in task execution.
   - Refines the task plan based on errors or feedback and retries until the task is successful.

---

## Installation

### Prerequisites
- Python 3.7 or higher.
- A valid Google Gemini API key.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-task-assistant.git
   ```
2. Install required dependencies:
   ```bash
   pip install google-genai
   ```
3. Replace `"Api_key"` in the code with your valid Gemini API key.

---

## Usage

### Run the Program
1. Navigate to the project directory:
   ```bash
   cd ai-task-assistant
   ```
2. Run the program:
   ```bash
   python ai_task_assistant.py
   ```

### Workflow
1. **Task Description**: Enter a description of the task you need help with (e.g., "Create and execute a Python program to print 'Hello, World!'.").
2. **Task Plan**: Review the AI-generated step-by-step task plan.
3. **Approval**:
   - Approve the plan by typing `yes`.
   - Request changes if needed (e.g., "Add comments in the code.") and refine the plan.
4. **Command Execution**: Enter the command to execute the task locally (e.g., `python hello_world.py`).
5. **Handle Errors**: If execution fails, provide feedback (e.g., "Correct the syntax error in the code.") to refine the plan and retry.

---

## Example

### Input:
Task Description: 
```text
Generate and execute a Python program to print "Hello, World!".
```

### Output Plan:
```text
Step 1: Create a file named hello_world.py with the following content:
        print("Hello, World!")
Step 2: Run the file using the command python hello_world.py.
```

### Execution:
Command:
```bash
python hello_world.py
```

Output:
```text
Hello, World!
```

---

## Error Handling

If the task fails, the assistant will:
1. Prompt for feedback on what went wrong.
2. Refine the task plan dynamically using AI based on feedback.
3. Retry the task until successful.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the functionality or extend features.





