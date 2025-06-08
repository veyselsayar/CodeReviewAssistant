import subprocess
import json

def analyze_code(code: str) -> dict:
    prompt = f"""
You are a helpful Python assistant. Please analyze the following Python code:

{code}

Tasks:
1. Check if the code has syntax or runtime errors.
2. If there are errors, provide the corrected code.
3. If there are no errors, confirm the code is valid.

Reply ONLY with a valid JSON object like this:

{{
  "has_error": true or false,
  "corrected_code": "corrected or original code as a string"
}}
"""

    process = subprocess.Popen(
        ['ollama', 'run', 'llama3.2'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=prompt)

    if process.returncode != 0:
        raise Exception(f'Ollama error: {stderr}')

    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return {'raw_output': stdout}
