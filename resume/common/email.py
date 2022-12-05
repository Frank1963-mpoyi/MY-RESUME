from threading import Thread
from django.conf import settings
from django.core.mail import send_mail


class ContactNotificationEmail(Thread):
    def __init__(self, name, email, message, messages_email):
        super(ContactNotificationEmail, self).__init__()
        # self.receiver = 'mpoyitshibuyi63@gmail.com'
        self.sender = settings.EMAIL_SENDER
        self.password = settings.EMAIL_PASSWORD
        self.name = name
        self.email = email
        self.message = messages_email
        self.email_from = email 
        self.subject = "Auto Response - Mpoyi Tshibuyi Resume - Do Not Reply"

        Thread.__init__(self)

    def run (self):
        self.name = self.name
        self.name = self.name.upper()
        
        send_mail(
            self.subject,
            self.message,
            self.sender,
            [self.email, ], # get automatic response
            fail_silently = False,
            auth_user = self.sender,
            auth_password = self.password
        )

        return 
