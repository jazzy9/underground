import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandboxe0fdd16ae4ed4f1baf0edcfe25b2e498.mailgun.org/messages",
		auth=("api", "068a1478ef2321af6b0bee1f6601e61a-e566273b-437890da"),
		data={"from": "Excited User <mailgun@https://app.mailgun.com/app/sending/domains/sandboxe0fdd16ae4ed4f1baf0edcfe25b2e498.mailgun.org>",
			"to": ["bar@example.com", "pip.c.brown@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})
