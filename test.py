import json 
import logging
import unittest
import convertvault
from convertion import Convert
from webtest import TestApp

class Test(unittest.TestCase):

    code= """$ANSIBLE_VAULT;1.1;AES256
63306532373363663238663465663630336562333464643039633735363231336664363736643765
3135646634363732346636643630353039353931623439350a303866636135316637663261636534
35316434393133313263393738313934353864336265666534356132383332303632326562373236
3932343138656535350a386361333831653838633362663139663062323230396337373231363866
3564"""
 
    def test_health(self):
        app = TestApp(convertvault.app)
        self.assertEqual(app.get('/health').status,"200 OK")

    def test_decode(self):
        conv = Convert('test')
        data = conv.convert(self.code)
        self.assertEqual(data['result'], 'toto')
        self.assertEqual(data['error'], '')

    def test_bad_decode(self):
        conv = Convert('test2')
        data = conv.convert(self.code)
        self.assertNotEqual(data['result'], 'toto')
        self.assertEqual(data['error'], 'La clé ne correspond pas')

if __name__ == '__main__':
    unittest.main()