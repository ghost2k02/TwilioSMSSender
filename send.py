import sys
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

def send_sms(recipient, message):
    try:
        # Use the Twilio API to send an SMS
        message = client.messages.create(
            body=message,
            from_="your_twilio_phone_number",  # Your Twilio phone number
            to=recipient
        )

        print(f"Message sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) < 3:
        print("Usage: send.py <recipient> <message>")
        sys.exit(1)

    recipient = sys.argv[1]
    message = ' '.join(sys.argv[2:])

    # Send SMS
    send_sms(recipient, message)
