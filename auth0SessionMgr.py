import requests
import threading

class Auth0Session:
    
    def __init__(self, auth0_id, auth0_secret, auth0_connection, auth0_domain):
        self.lock = threading.Lock()
        
        #get this data out of the Auth0 portal
        self.auth0_id = auth0_id # Client ID under application management
        self.auth0_connection = auth0_connection # string representing the name of the application in Aplication mgmt
        self.auth0_domain = auth0_domain #Domain under Application mgmt - e.g. acme.auth0.com
        
        ######################################
        ## Do Not Store This Anywhere In Your Code!!!!
        ## No one should see this secret ever! Definately do not deploy this in a front end anywhere!
        self.auth0_secret = auth0_secret #Client Secret under application management

        self.s = requests.Session()
        

        
        
    def login(self, username, password, userid, domain):
        
        self.username = username
        self.password = password
        self.userid = userid
        self.domain = domain
        session = requests.Session()
        # first we have to get an auth token from Auth0
        try:
            
            #we have to make a call to Auth0 in order to get a session token
            r = session.post(
                'https://'+auth0_domain+'/oauth/token',
                json={
                    'client_id': self.auth0_id,
                    'username': self.username,
                    'password': self.password,
                    'connection' : auth0_connection,
                    'client_secret': self.auth0_secret,
                    'grant_type': 'password' #we are using password authentication
                },
                headers={'Content-Type': 'application/json'}
            )
        except requests.exceptions.RequestException as e:
            print(r)
            print (r.text)
            return e
        
        #if the call is successful, we will get back a session token from auth0 that we can use
        # to register a session directly with our app now
        data = r.json()
        self.token = data['id_token']
        
        #now we have an access token, we can use it to call our application to get a session
        # to get the correct formatting of this call, you need to use Chrome Dev Tools to
        # monitor your application during login, and see what calls are being made
        #
        # here's an example structure
        self.headers = { 'authorization' : 'Bearer ' + self.token }
        r = requests.get('https://acme.com/api/v1/', headers=self.headers, verify=False)
        
        #print(url)
        try:
            r2 = self.s.get(url)
        except requests.exceptions.RequestException as e:
            print(r)
            print (r.text)
            return e
        return
    
   

    #####################################################################3
    #
    # wrap a post in the existing authenticated session
    #
    def post(self, url, payload):
        
        self.lock.acquire()
        try: 
            r = self.s.post(url, data=payload, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print(r)
            print (r.text)
            return e
        finally:
            self.lock.release()
        print (r)
        
    
    
    #####################################################################3
    #
    # wrap a get in the existing authenticated session
    #
    def get(self, url, payload=None):
        self.lock.acquire()
        try:
            r = self.s.post(url, data=payload, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print(r)
            print (r.text)
            return e
        finally:
            self.lock.release()

        print (r)
      
            
   
