from pegar_id_posts import get_post_ids
from pegar_comentarios import get_comments
from comando_dl import seach_command
from pegar_image_git import git_get_image
from legendar_image import legendar_image
from fb_imgbb_upload import imgBB, armazenar_image_fb, publicar_image_fb
import asyncio


async def test():
    post_ids = await get_post_ids()
    
    ids, comments = await get_comments(post_ids)
    sub_ids, sub_comments = await get_comments(ids)
    
    ids.extend(sub_ids)
    comments.extend(sub_comments)
    # fazer uma verficação aqui dos ids ja respondidos
    frames = seach_command(ids, comments)
    await git_get_image(frames)
                                            
    for f in frames:         # frames [['5', 'frame_500.jpg', '', '379148288497935_432280169616424']]
        episodio = f[0]
        frame = f[1]
        captions = f[2]
        id_comentario = f[3]
        
        legendar_image(frame, captions)
        
        if captions != '':
            frame = f's{frame}'

            link = imgBB(frame)
            foto_id = armazenar_image_fb(frame)
        else:
            link = imgBB(frame)
            foto_id = armazenar_image_fb(frame)
        
        
        estado = publicar_image_fb(episodio, frame, link, foto_id, id_comentario)
        
        if estado == True:
            print('comentario respondido com sucesso')
            
            
        

    

def main():
    asyncio.run(test())


main()
