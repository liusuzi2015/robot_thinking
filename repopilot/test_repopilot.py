# Importing the RepoPilot library
import repopilot

# Initialize RepoPilot with the path to your code repository
repo_path = "/Users/lanyingsu/Documents/dev/ai_agent/repository/RepoPilot"
rp = repopilot.RepoPilot(repo_path)

# Example 1: Natural Language Query about a Feature
# User asks about the login feature in a conversational manner
query = "请解释代码库中ZoektServer的功能."
login_feature_explanation = rp.query_codebase(query)
print("Login Feature Explanation:")
print(login_feature_explanation)