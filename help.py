import httpx
from database import Data


def help(id_comentario, message):

    data = {
       'message': message,
       'access_token': Data.fb_access_token  
    }
    
    try:
        response = httpx.post(f'{Data.fb_url}/{id_comentario}/comments', data=data, timeout=10)
        
        if response.status_code == 200:
            print('Comment posted successfully')
        else:
            print(f'Failed to post comment: {response.status_code}')
            print(response.json())
            print(response.content)
    
    except httpx.RequestError as e:
        print(f'HTTP request error: {e}')
    except Exception as e:
        print(f'Error: {e}')

    
                    
        
                    
