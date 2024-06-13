from database import Data
import asyncio, httpx


async def fetch_comments(session: httpx.AsyncClient, post_id: str) -> dict:
    """
    Fetches comments for a given Facebook post ID.

    Args:
        session (httpx.AsyncClient): The HTTP client session.
        post_id (str): The ID of the Facebook post.

    Returns:
        dict: The response data containing comments.
    """
    url = f'{Data.fb_url}/{post_id}/comments?limit=50&access_token={Data.fb_access_token}'
    response = await session.get(url)
    response_data = response.json()
    return response_data

async def get_comments(new_ids: list[str]) -> tuple[list[str], list[str]]:
    """
    Retrieves comments and their IDs for a list of Facebook post IDs.

    Args:
        new_ids (List[str]): A list of Facebook post IDs.

    Returns:
        Tuple[List[str], List[str]]: Two lists, one with comment IDs and one with messages.
    """
    comments_ids = []
    messages = []
    
    async with httpx.AsyncClient() as session:
        tasks = [fetch_comments(session, post_id) for post_id in new_ids]
        responses = await asyncio.gather(*tasks)
        
        for response_data in responses:
            for item in response_data['data']:
                comments_ids.append(item['id'])
                messages.append(item['message'])

    print('terminou o get_comments')
    return comments_ids, messages
