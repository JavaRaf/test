from database import Data
import httpx, asyncio


async def get_post_ids():
    post_ids = []
    dados = {'limit': '100', 'access_token': Data.fb_access_token}

    while Data.init < Data.max:
        async with httpx.AsyncClient() as session:
            response = await session.get(f'{Data.fb_url}/{Data.page_id}/posts/', params=dados, timeout=20)
            if response.status_code == 200:
                response_data = response.json()
                
                for item in response_data.get('data', []):
                    post_ids.append(item['id'])

                if 'paging' in response_data and 'next' in response_data['paging']:
                    after = response_data['paging']['cursors']['after']
                    dados['after'] = after 
                    dados['limit'] = 100 
                    Data.init += 1
                else:
                    break
            else:
                print('error: loop qubrado')
                break  # se a resposta não for 200, interrompe o loop
    
    Data.init = 0                             
    return post_ids
        

