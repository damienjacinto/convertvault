import logging
import sys
from ansible.constants import DEFAULT_VAULT_ID_MATCH
from ansible.parsing.vault import VaultSecret, VaultLib

class Convert:
   def __init__(self, password):
      self.text = b''
      self.err = ''
      self.password = password
      if password:
         self.vault = VaultLib([(DEFAULT_VAULT_ID_MATCH, VaultSecret(password.encode("utf-8")))])

   def convert(self, source):
      try:
         if self.vault and source:
            self.decrypt(source) if source.startswith("$ANSIBLE_VAULT") else self.encrypt(source)
      finally:
         return {'password': self.password, 'source': source, 'result': self.text.decode('utf-8'), 'error': self.err}

   def encrypt(self, source):
      logging.debug("Request encrypt")
      try:
         self.text = self.vault.encrypt(source)
      except:
         self.err = "Impossible de chiffrer ces informations"
         logging.error("Problem: %s", sys.exc_info()[0]) 

   def decrypt(self, source):
      logging.debug("Request decrypt")
      try:
         self.text = self.vault.decrypt(source)
      except:
         self.err = "La clé ne correspond pas"
         logging.error("Problem: %s", sys.exc_info()[0])