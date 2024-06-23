from database import Data
import asyncio
import httpx

async def fetch_comments(session: httpx.AsyncClient, post_id: str, semaphore: asyncio.Semaphore) -> dict:
    url = f'{Data.fb_url}/{post_id}/comments?limit=50&access_token={Data.fb_tok}'
    async with semaphore:
        try:
            response = await session.get(url, timeout=20)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred for post_id {post_id}: {exc}")
        except asyncio.CancelledError:
            print(f"Request for post_id {post_id} was cancelled.")
            raise  # Re-raise the CancelledError to propagate it
        except Exception as exc:
            print(f"An error occurred for post_id {post_id}: {exc}")
        return {}  # Return an empty dictionary in case of errors

async def get_comments(new_ids: list[str]) -> tuple[list[str], list[str]]:
    comments_ids = []
    messages = []

    semaphore = asyncio.Semaphore(100)  # Limit of 100 concurrent requests

    async with httpx.AsyncClient() as session:
        tasks = [fetch_comments(session, post_id, semaphore) for post_id in new_ids]
        responses = await asyncio.gather(*tasks, return_exceptions=True)  # Return exceptions for better error handling

        for response_data in responses:
            if isinstance(response_data, dict) and 'data' in response_data:
                for item in response_data['data']:
                    if item:
                        comments_ids.append(item.get('id', ''))
                        messages.append(item.get('message', ''))

    return comments_ids, messages

