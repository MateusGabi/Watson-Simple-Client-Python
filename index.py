import json
import watson_developer_cloud
import os
from dotenv import load_dotenv

#
# configure .env
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

#
# setting vars
watson_username = os.environ.get("WATSON_USERNAME")
watson_password = os.environ.get("WATSON_PASSWORD")
watson_workspace_id = os.environ.get("WATSON_WORKSPACE_ID")

#
# setting watson conversation
conversation = watson_developer_cloud.ConversationV1(
    username=watson_username,
    password=watson_password,
    version='2018-02-16'
)

response = conversation.message(
    workspace_id=watson_workspace_id,
    input={
        'text': 'Hello'
    }
)

print(json.dumps(response, indent=2))