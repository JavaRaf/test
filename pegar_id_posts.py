import httpx
import time
from database import Data

def get_post_ids():
    comments_ids = []
    comments = []
    
    # "136437712888196_122186265332068249" id do post de download
    
    # Get page ID
    response = httpx.get(f'{Data.fb_url}/me?access_token={Data.fb_tok}')
    if response.status_code == 200:
        page_id = response.json().get('id', [])
    else:
        print(f"Failed to get page ID: {response.status_code}") 
        return
    
    dados = {'fields': 'comments.limit(50)', 'limit': '100', 'access_token': Data.fb_tok}
    try:
        
        while Data.init < Data.max:
            response = httpx.get(f'{Data.fb_url}/{page_id}/posts/', params=dados)
            if response.status_code == 200:
                response_data = response.json()
                
                for item in response_data.get('data', []):
                    comments_data = item.get('comments', {}).get('data', [])
                    if len(comments_data) >= 1:
                        for comment in comments_data:
                            if 'id' in comment:
                                comments.append(comment.get('message'))
                                comments_ids.append(comment.get('id'))
                
                # Check for pagination
                if 'paging' in response_data and 'next' in response_data['paging']:
                    after = response_data['paging']['cursors'].get('after', '')
                    dados['after'] = after
                    Data.init += 1
                else:
                    break
            else:
                print(f"Failed to get posts: {response.status_code}")
                break
            
            time.sleep(1)
              
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc}")
    except Exception as exc:
        print(f"An error occurred: {exc}")
                
    Data.init = 0
    
    return comments_ids, comments


