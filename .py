import httpx
import asyncio
from database import Data
from pegar_id_posts import get_post_ids 
from pegar_comentarios import get_comments

async def test():
    post_ids = await get_post_ids()
    id, comments = await get_comments(post_ids)
    
    for id, comments in zip(id, comments):
        if comments.startswith('!'):
            print(comments)
    


asyncio.run(test())
    