from pegar_id_posts import get_post_ids
from pegar_comentarios import get_comments
from comando_dl import seach_command
from pegar_image_git import git_get_image
from legendar_image import legendar_image
from fb_imgbb_upload import imgBB, armazenar_image_fb, publicar_image_fb
from carregar_ids import carregar, save_ids_to_txt
import asyncio, time
from push_github import git_push_ids


async def test():
    
    inicio = time.time()
    
    comments_ids, comments = get_post_ids()
    
    comments_ids.append('136437712888196_122186265332068249')  # id do post fixado sobre download
    comments.append('post fixado sobre download')
    
    fim = time.time()
    print(f'Tempo de execução do post_ids foi: {fim - inicio:.2f} segundos\n')

    inicio2 = time.time()
    ids, sub_comments = await get_comments(comments_ids)
    print('Terminou o get_comments\n')

    fim2 = time.time()
    
    print(f'Tempo de execução do get_comments foi: {fim2 - inicio2:.2f} segundos\n')
    
    comments_ids.extend(ids)
    comments.extend(sub_comments)
    
    new_comments_ids, new_comments = carregar(comments_ids, comments) #  verficação dos ids ja respondidos
    
    frames = seach_command(new_comments_ids, new_comments)
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
            save_ids_to_txt(id_comentario)
            git_push_ids()
            
            
            
def main():
    start_time = time.time()
    while (time.time() - start_time) < (180 * 60):
        asyncio.run(test())

        print('esperando 50 segundos')
        time.sleep(50)
        
main()
