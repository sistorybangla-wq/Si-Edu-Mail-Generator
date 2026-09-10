import requests
import json
import urllib3
import string
import random
import time
from __colors__.colors import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class EduHelper:
    def __init__(self, id):
        # Updated User-Agent for 2026
        self.url = 'https://www.openccc.net/f-vs-stand-I-hat-of-yout-ands-Banquoh-Cumberland?d=www.openccc.net'
        self.h = {
            'accept': 'application/json; charset=utf-8',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'content-type': 'text/plain; charset=utf-8',
            'origin': 'https://www.openccc.net'
        }

        self.url1 = 'https://www.openccc.net/cccacct-proxy/createAccount?locale=en&source=https://www.opencccapply.net/SSOLogin/{idd}/false/en'.format(idd=id)

        
        self.urlxd = 'https://www.openccc.net/cccacct-proxy/createAccount?locale=en&source=https://www.opencccapply.net/SSOLogin/{idd}/false/en'.format(idd=id)

        self.url2 = 'https://www.openccc.net/f-vs-stand-I-hat-of-yout-ands-Banquoh-Cumberland?d=www.openccc.net'

        self.h2 = {
            'accept': 'application/json; charset=utf-8',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'content-type': 'text/plain; charset=utf-8',
            'origin': 'https://www.openccc.net',
            'sec-fetch-site': 'same-origin'
        }
        
        self.url3 = 'https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/action.uP?pP_execution=e1s1'
        self.h3 = {
            'origin': 'https://www.openccc.net',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin'
        }
        self.cookie = {
            'reese84': None
        }

        self.session = requests.Session()
    
    def getAuthToken(self):
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Fetching Token (2026 Version)', end='')
        try:
            data = {
                'solution': {
                    'interrogation': {
                        'p': ''.join(random.choices(string.ascii_lowercase + string.digits, k=40)),
                        'st': int(time.time()),
                        'sr': random.randint(1000000000, 9999999999),
                        'cr': random.randint(100000000, 999999999)
                    },
                    'version': 'stable'
                },
                'old_token': None,
                'error': None,
                'performance': {
                    'interogation': 248
                }
            }

            res = self.session.post(url=self.url, data=json.dumps(data), headers=self.h, verify=False, timeout=10)
            
            js = res.json()
            token = js['token']
            self.cookie['reese84'] = token
            print(fg + ' (success)')
            return token
        except Exception as e:
            print(fr + ' (failed: ' + str(e) + ')')
            return None
    
    def _tryHarder(self):
        token = self.getAuthToken()
        if token is None:
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fr + 'Token acquisition failed')
            return None, None, None
            
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Fetching Cookies', end='')
        try:
            self.session.get(url=self.url1, cookies=self.cookie, headers=self.h, verify=False, timeout=10)
            print(fg + ' (success)')
        except Exception as e:
            print(fr + ' (failed: ' + str(e) + ')')

        data2 = '"{tok}"'.format(tok=token)
        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Sending Custom Fields and Token to Server', end='')
        try:
            resp = self.session.post(url=self.url2, data=data2, headers=self.h2, verify=False, timeout=10)
            print(fg + ' (success)')
            js = resp.json()
            print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Setting Incap Token', end='')
            token = js['token']
            self.cookie['reese84'] = token
            print(fg + ' (success)')
        except Exception as e:
            print(fr + ' (failed: ' + str(e) + ')')
            return None, None, None

        print(fc + sd + '[' + fm + sb + '*' + fc + sd + '] ' + fg + 'Sending Custom Cookies', end='')
        data3 = '_eventId_continue=&flowId=e1s1'
        try:
            resp3 = self.session.post(url=self.url3, data=data3, headers=self.h3, cookies=self.cookie, verify=False, timeout=10)
            print(fg + ' (success)')
        except Exception as e:
            print(fr + ' (failed: ' + str(e) + ')')
            return None, None, None

        return resp3.url, self.session.cookies, token
