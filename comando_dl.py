import re
from help import help
from carregar_ids import save_ids_to_txt
from tenor_gif import get_random_frieren_gif
from push_github import git_push_ids

HELP_MESSAGE = (
    "\n\nHelper:\n\n"
    "-e [Episode]: required\n"
    "-f [Frame]: required\n"
    "-t [Text]: optional, but required if using double quotes\n\n"
    "Example:\n\n"
    "!dl -e 15 -f 2500  # for frame only\n"
    "or\n"
    "!dl -e 15 -f 2500 -t \"my text here\"  # for frame with text\n\n"
    "!dl -h  # for this help\n"
    "!gif  # for a Frieren gif\n"
    "or\n"
    "!gif \"Fern\"  # for a Fern gif or a gif about anything\n\n"
)

def extract_episode_frame(message: str) -> tuple[str, str, str]:
    episodio, frame, captions = '', '', ''
    numeros = re.findall(r'\d+', message)
    
    if len(numeros) == 2:
        episodio = numeros[0]
        frame = f'frame_{numeros[1]}.jpg'
        
        if '-t' in message:
            result = re.findall(r'"(.*?)"', message)
            captions = ' '.join(result)
    
    return episodio, frame, captions

def handle_help_command(id: int) -> None:
    link_gif = get_random_frieren_gif(tag='anime Frieren')
    help_message = HELP_MESSAGE + link_gif
    help(id, help_message)

def handle_gif_command(id: int, message: str) -> None:
    tag = re.findall(r'"(.*?)"', message)
    tag = tag[0] if tag else 'anime Frieren'
    link_gif = get_random_frieren_gif(tag)
    
    gif_message = f'Random gif about {tag} :\n{link_gif}'
    help(id, gif_message)

def seach_command(ids: list, comments: list) -> list[str]:
    frames = []

    for id, message in zip(ids, comments):
        
        if ('Helper:' not in message):
        
            if ('!dl' in message) and ('-e' in message) and ('-f' in message):
                
                print('comands:', message)
                
                episodio, frame, captions = extract_episode_frame(message)
                if episodio and frame:
                    frames.append([episodio, frame, captions, id])
            
            elif ('!dl' in message) and ('-h' in message):
                
                print('comands:', message)
                
                handle_help_command(id)
                save_ids_to_txt(id)
                git_push_ids()
                
            
            elif message.lower().startswith('!gif'):
                
                print('comands:', message)
                
                handle_gif_command(id, message)
                save_ids_to_txt(id)
                git_push_ids()
            
    return frames
