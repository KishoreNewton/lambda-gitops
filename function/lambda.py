  
from github import Github

def lambda_handler(event, context):
    if event["input"] == "Hello":
        return "World"
    else:
        raise
