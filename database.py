import os


class Data:
    
    
    #facebook
    fb_access_token = os.environ.get('fb_tok')
    fb_version = 'v19.0'
    fb_url = f'https://graph.facebook.com/{fb_version}'
    
    
    #github
    git_username = 'JavaRaf'
    git_repo_name = 'SNF' # nome do repositorio onde estao os frames
    git_branch = 'main' # branch deste repositorio
    git_this_repo = 'test'
    git_token = os.environ.get('git_tok')
    
    
    #tenor gifs
    tenor_token = os.environ.get('gif_tok')

    #imgBB
    img_url = 'https://api.imgbb.com/1/upload' 
    img_token = os.environ.get('imgbb_tok')


    #othes 
    init = 0   # usado para pegar os posts_ids
    max = 30  # cada interação pega no maximo 50 comentarios por post