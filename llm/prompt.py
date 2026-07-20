def build_prompt(requirements):

    prompt = f"""
Generate software test cases.

Requirement:
{requirements}

Generate exactly 3 test cases.

Use this format:

Test Case ID:
Scenario:
Steps:
1.
2.
3.

Expected Result:

Example:

Test Case ID: TC001
Scenario: Successful login
Steps:
1. Open login page
2. Enter valid username
3. Enter valid password
4. Click login button

Expected Result:
User should login successfully.

Now generate new test cases for the requirement.
"""

    return prompt