import ssl
from django.core.mail.backends.smtp import EmailBackend

class UnverifiedEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(
                self.host, self.port, timeout=self.timeout
            )
            self.connection.set_debuglevel(1) 
            if self.use_tls:
                self.connection.ehlo()
                self.connection.starttls(context=ssl._create_unverified_context())
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silently:
                raise
            return False