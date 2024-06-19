import os, httpx



class Data:
    
    
    #facebook
    fb_tok = os.environ.get('FB_TOK')
    fb_version = 'v19.0'
    fb_url = f'https://graph.facebook.com/{fb_version}'
    

    #github
    git_username = 'JavaRaf'
    git_repo_name = 'SNF' # nome do repositorio onde estao os frames
    git_branch = 'main' # branch deste repositorio
    git_this_repo = 'test'
    git_token = os.environ.get('GIT_TOK')
    
    #tenor gifs
    gif_tok = os.environ.get('GIF_TOK')

    #imgBB
    img_url = 'https://api.imgbb.com/1/upload' 
    imgbb_tok = os.environ.get('IMGBB_TOK')

    #othes 
    init = 0   # usado para pegar os posts_ids
    max = 7  # cada interação pega no maximo 50 comentarios por post