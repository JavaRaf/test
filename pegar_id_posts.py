from database import Data
import httpx


def get_post_ids():
    post_ids = []
    dados = {'limit': '100', 'access_token': Data.fb_access_token}
    
    #get_page_id
    response = httpx.get(f'{Data.fb_url}/me?access_token={Data.fb_access_token}')
    page_id = response.json().get('id')
    
    try:
        while Data.init < Data.max:
            response = httpx.get(f'{Data.fb_url}/{page_id}/posts/', params=dados, timeout=15)
            
            if response.status_code == 200:
                response_data = response.json()
                
                for item in response_data.get('data', []):
                    post_ids.append(item.get('id', ''))
                
                if 'paging' in response_data and 'next' in response_data['paging']:
                    after = response_data['paging']['cursors'].get('after', '')
                    dados['after'] = after
                    Data.init += 1
                        
                else:
                    break  # Break the loop if no more paging 
                     
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc}")
    except Exception as exc:
        print(f"An error occurred: {exc}")
                
    Data.init = 0
    return post_ids




