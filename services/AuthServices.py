from appwrite.client import Client
from appwrite.services.account import Account
from appwrite.id import ID
from utils.logger import setup_logger 
from helpers import save_session_encrypted,load_session_encrypted
import os


class AuthServices:
    def __init__(self):
        self.logger = setup_logger()
        self.__APPWRITE_ENDPOINT="https://cloud.appwrite.io/v1"
        self.__PROJECT_ID = "673198560005a6f1b910"
        self.__client=Client()
        self.__client.set_endpoint(self.__APPWRITE_ENDPOINT).set_project(self.__PROJECT_ID)
        self.account = Account(self.__client)
    def register(self,email,password,name):
        try:
            user = self.account.create(
                user_id=ID.unique(),
                email=email,
                password=password,
                name=name
            )
            if user:
                # Create session after successful registration
                session = self.account.create_email_password_session(email, password)
                save_session_encrypted(session)
                self.logger.info(f"User registered successfully: {email}")
                return session
        except Exception as error:
            self.logger.error(f"Registration error: {str(error)}")
            raise Exception(f'Could not register user: {str(error)}')
    def login(self, email, password):
        try:
            session = self.account.create_email_password_session(email=email, password=password)
            save_session_encrypted(session)
            self.logger.info(f"User logged in successfully: {email}")
            return session
        except Exception as error:
            self.logger.error(f"Login error: {str(error)}")
            raise Exception(f'Could not login user: {str(error)}')
        
    def logout(self):
        try:
            os.remove("session.txt")
            self.logger.info("User logged out successfully")
        except Exception as error:
            self.logger.error(f"Logout error: {str(error)}")
            raise Exception(f'Could not logout user: {str(error)}')
    def get_user(self):
       try:
          user = load_session_encrypted()
          return user
       except Exception:
        return None

    def is_authenticated(self):
     try:
        session = load_session_encrypted()
        if not session:
            self.logger.info("No session found, user is not authenticated.")
            return False
        self.logger.info(f"is_authenticated check | Retrieved User:")
        return True
     except Exception as error:
        self.logger.error(f"is_authenticated error: {error}")
        return False

        

def auth():
    return AuthServices()