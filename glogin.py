import requests
from bs4 import BeautifulSoup


def login(id,pwd):
  class SessionGoogle:
      def __init__(self, url_login, url_auth, login, pwd):
          self.ses = requests.session()
          login_html = self.ses.get(url_login)
          soup_login = BeautifulSoup(login_html.content, features="html5lib").find('form').find_all('input')
          my_dict = {}
          for u in soup_login:
              if u.has_attr('value'):
                  my_dict[u['name']] = u['value']
          my_dict['Email'] = login
          my_dict['Passwd'] = pwd
          self.ses.post(url_auth, data=my_dict)

      def get(self, URL):
          return self.ses.get(URL).text


  url_login = "https://mail.google.com/mail/u/0/"
  url_auth = "https://accounts.google.com/v3/signin/"
  session = SessionGoogle(url_login, url_auth, id, pwd)
  if id in session.get("http://mail.google.com/mail/u/0"): return True
  else: return False