import httpx
from database import Data




def imgBB(frame):
    try:
        
        frame_name = frame.replace('.jpg', '')
        data = {'key': Data.img_token, 'name': f'{frame_name}', 'expiration': 600000}

        with open(f'images/{frame}', 'rb') as file:
            files = {'image': file}
            
            response = httpx.post(Data.img_url, data=data, files=files, timeout=10)
            if response.status_code == 200:
                response_data = response.json()
                link = response_data['data']['url']
                print('imagem enviada pro o imgbb')
                return link
                
            else:
                print('erro no imgbb', response.status_code)
                print(response.content)
                return ''
    except FileNotFoundError:
        print(f"O arquivo ./images/{frame} não foi encontrado.")
        return ''

def armazenar_image_fb(path_to_frame: str): 
    try:
        
        # Verificar se o caminho fornecido está correto
        with open(f'./images/{path_to_frame}', 'rb') as frame:
            files = {'file': (path_to_frame, frame, 'image/jpeg')}
            
            data = {
                'published': 'false',
                'access_token': Data.fb_access_token
            }
            
            response = httpx.post(f'{Data.fb_url}/me/photos', files=files, data=data, timeout=10)
            
            if response.status_code == 200:
                foto_id = response.json().get('id')
                if foto_id:
                    return foto_id
            else:
                print(f'Erro ao fazer upload: {response.status_code}')
                print(f'Resposta: {response.text}')
        
    except FileNotFoundError:
        print(f'Arquivo {path_to_frame} não encontrado')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        
        
def publicar_image_fb(episodio: str, frame: str, link: str, foto_id: str, id_comentario: str): # espera o id da image armazenada pela funçao acima, id do comentario a ser respondido
    
    frame = frame.replace('s', '').replace('frame_', '').replace('.jpg', '')
    
    message = f'Filename: Episode {episodio}, Frame {frame} \n\n Resolution: 1920x1080 \n Link: {link}'

    data = {
        'message': message,
        'attachment_id': foto_id,
        'access_token': Data.fb_access_token
    }
    response = httpx.post(f'{Data.fb_url}/{id_comentario}/comments', data=data, timeout=10)
   
    if response.status_code == 200:
        return True
    else:
        print('erro ao enviar a imagem pro fb', response.status_code)
        print(response.content) 
        return False



