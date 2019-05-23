def send_simple_message():
    return requests.post("https://api.mailgun.net/v3/sandboxd8603bb5714a4eb18e58db705e9688e8.mailgun.org/messages",
        auth=("api","93fdb1c517a7bd307ed8e12cee162f8b-e566273b-ba4c284f"),
        data={"from": "Excited User <mailgun@sandboxd8603bb5714a4eb18e58db705e9688e8.mailgun.org>",
                "to": ["bar@example.com"],
                "subject": "Hello",
                "text": "Testing some Mailgun awesomness!"})
