from database import Data
import httpx, asyncio


async def get_post_ids():
    post_ids = []
    dados = {'limit': '100', 'access_token': Data.fb_access_token}
    session = httpx.AsyncClient()

    try:
        while Data.init < Data.max:
            response = await session.get(f'{Data.fb_url}/{Data.page_id}/posts/', params=dados, timeout=20)
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
            else:
                print(f'HTTP error: {response.status_code} - {response.reason_phrase}')
                break  # Break the loop if non-200 status code
    
    except httpx.HTTPStatusError as exc:
        print(f"HTTP error occurred: {exc}")
    except Exception as exc:
        print(f"An error occurred: {exc}")
    finally:
        await session.aclose()  # Close the session at the end

    Data.init = 0
    return post_ids

