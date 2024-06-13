import httpx, json
from database import Data
import random



def get_random_frieren_gif(tag):
     
    # URL da API para busca de GIFs
    url = f"https://tenor.googleapis.com/v2/search?q={tag}&key={Data.tenor_token}&client_key=my_test_app&limit=50"

    try:
        # Fazendo a requisição HTTP
        response = httpx.get(url, timeout=15)

        if response.status_code == 200:
            # Carrega os GIFs usando os URLs dos tamanhos menores
            gifs_data = response.json().get('results', [])

            # Escolhe um GIF aleatório dos resultados disponíveis
            if gifs_data:
                random_gif = random.choice(gifs_data)
                gif_url = random_gif.get('url')

                return gif_url
            else:
                print("Nenhum GIF encontrado para o termo de busca.")
        else:
            print(f"A requisição falhou com status code: {response.status_code}")

    except httpx.RequestError as e:
        print(f"Erro ao fazer requisição HTTP: {e}")

    return None



