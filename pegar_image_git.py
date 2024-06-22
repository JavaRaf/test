import httpx, asyncio
from database import Data




async def git_fetch_image(session, url, frame):
    response = await session.get(url)
    if response.status_code == 200:
        with open(f'./images/{frame}', 'wb') as file:
            file.write(response.content)

async def git_get_image(frames):
    async with httpx.AsyncClient() as session:  # list_frames exemplo ([episodio, frame_number, captions, id])
        tasks = []
        for item in frames:
            episodio = f'EP-{int(item[0])}'
            frame = item[1]

            if episodio and frame:
                url = f'https://raw.githubusercontent.com/{Data.git_username}/{Data.git_repo_name}/{Data.git_this_branch}/{episodio}/{frame}'
                tasks.append(git_fetch_image(session, url, frame))
                
        await asyncio.gather(*tasks)