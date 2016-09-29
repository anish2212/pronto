# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC471b4009becda2f23c3fe90df58dd7cc"
auth_token = "dae6dc2569f846ab2b9e2404c7b1d876"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+16264752489", from_="+14159432584",
                                     body="This is from Pronto's Twilio test app!")
                                     
                                     
from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)