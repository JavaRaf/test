from database import Data
import httpx



async def get_post_ids() -> list[str]:
    post_ids = []
    # here you can put an specific post id to your bot to monitoring
    dados = {'limit': '100', 'access_token': Data.fb_access_token}

    while Data.init < Data.max:
        responses = []
        
        async with httpx.AsyncClient() as session:
            response = await session.get(f'{Data.fb_url}/me/posts/', params=dados)
            if response.status_code == 200:
                response_data = response.json()
                responses.append(response_data)
                
                if 'next' in response_data['paging']: 
                    after = response_data['paging']['cursors']['after']
                    dados['after'] = after 
                    dados['limit'] = 100 
                    Data.init += 1
                else:
                    break
                                            
    for response in responses:        
        for item in response['data']:
            post_ids.append(item['id'])
            
    return post_ids