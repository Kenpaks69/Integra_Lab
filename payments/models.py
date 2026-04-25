from django.db import models
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

class Payment(models.Model):
   cardholder_name = models.CharField(max_length=100)
   encrypted_card_number = models.BinaryField()

   def set_card_number(self, plain_text):
    self.encrypted_card_number = cipher.encrypt(plain_text.encode())

    def get_card_number(self):
        return cipher.decrypt(self.encrypted_card_number).decode()
