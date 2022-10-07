from os import environ

from whatsapp_api_client_python import API as RestApi

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = RestApi.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def main():
    restApi.sending.sendMessage('120363025955348359@g.us', 'Message text')

if __name__ == "__main__":
    main()