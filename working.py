from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)
account_sid = "AC471b4009becda2f23c3fe90df58dd7cc"
auth_token = "dae6dc2569f846ab2b9e2404c7b1d876"
from_number = "+14159432584"

client = TwilioRestClient(account_sid, auth_token)

def send_sms(to_number, message_body):
    client.messages.create(
        to=to_number, 
        from_=from_number,
        body=message_body    
    )    

@app.route("/", methods=['GET', 'POST'])
def receieve_sms():
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    send_sms(from_number, body)
    return None
    
"""
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)
"""
    
if __name__ == "__main__":
    app.run(debug=True)