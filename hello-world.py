from flask import Flask
from flask import request, make_response
import os
import json

app = Flask(__name__)


#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"
    
@app.route("/slackbutton", methods=['POST'])
def respond():
    """
    This route listens for incoming message button actions from Slack.
    """    
    response_msg = json.loads(request.form["payload"])

    parameters = {"name": response_msg['user']['id'], "time": response_msg['actions'][0]['value']}    
    command = "ansible-playbook send-message.yml --connection=local --extra-vars \"" + str(parameters) + "\""
   
    os.system(command)
    return make_response("OK",200)
    
if __name__ == "__main__":
	app.run()
