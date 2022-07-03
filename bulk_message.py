from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep


CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(API_NAME, API_VERSION, SCOPES)

print("""

 ___                                        __               ___                                                       
|     |.-----.---.-.----.----.-----.--.--.--.|    \.--.--.|  |  |--.|    _|.--------.---.-.||  |.-----.-----.-----.--|  |.-----.----.
|     ||  _  |  _  |   |   _|  _  |  |  |  ||    <|  |    |    < |    __        |  _    |  ||_ --|  -_|     |  _    -|   _|
|__||   |_.|| || |__|__||__/|_||||||__|||||_.|||||_|_|||_||__||  
         ||                                                                                                                                


""")


n = int(input('Number of recipients : '))
for i in range(n):
    mail_id = input('{} recipient email :'.format(i))


subject = input('Subject : ')
message = input('Type the message : ')
mimeMessage = MIMEMultipart()
mimeMessage['to'] = mail_id
mimeMessage['subject'] = subject
mimeMessage.attach(MIMEText(message, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()

print('Mail is senting .....')

sleep(4)
print('Completed')
