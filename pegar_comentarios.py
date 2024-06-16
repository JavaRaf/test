from database import Data
import asyncio
import httpx


async def fetch_comments(session: httpx.AsyncClient, post_id: str, semaphore: asyncio.Semaphore) -> dict:

    url = f'{Data.fb_url}/{post_id}/comments?limit=50&access_token={Data.fb_access_token}'
    async with semaphore:
        try:
            response = await session.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred: {exc}")
        except Exception as exc:
            print(f"An error occurred: {exc}")
        return {}

async def get_comments(new_ids: list[str]) -> tuple[list[str], list[str]]:

    comments_ids = []
    messages = []

    semaphore = asyncio.Semaphore(100)  # Limite de 100 requisições simultâneas

    async with httpx.AsyncClient() as session:
        tasks = [fetch_comments(session, post_id, semaphore) for post_id in new_ids]
        responses = await asyncio.gather(*tasks)

        for response_data in responses:
            if 'data' in response_data:
                for item in response_data['data']:
                    comments_ids.append(item['id'])
                    messages.append(item['message'])

    return comments_ids, messages
