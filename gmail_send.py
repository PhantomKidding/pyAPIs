import argparse
import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools


class Gmail:

    SCOPES = 'https://mail.google.com/'
    CLIENT_SECRET_FILE = 'fattywhitysmarty.json'
    APPLICATION_NAME = 'Notifier'

    def __init__(self, sender):
        self._flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args([])
        self._sender = sender

    def get_credentials(self, credential_file='fattywhitysmarty.credentials'):
        store = file.Storage(credential_file)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if self._flags:
                credentials = tools.run_flow(flow, store, self._flags)
            else:  # Needed only for compatability with Python 2.6
                credentials = tools.run(flow, store)
                # print 'Storing credentials to ' + credential_path
        return credentials

    @staticmethod
    def create_message(sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.b64encode(message.as_string())}

    def send_message(self, to, subject, message_text):
        credentials = self.get_credentials()
        service = build('gmail', 'v1', http=credentials.authorize(Http()))
        message = self.create_message(self._sender + '@gmail.com', to, subject, message_text)
        return service.users().messages().send(userId='me', body=message).execute()

# test
# gmail = Gmail('fattywhitysmarty').send_message('fattywhitysmarty@gmail.com', 'test', 'test')
