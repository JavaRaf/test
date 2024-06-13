import re
from help import help
from tenor_gif import get_random_frieren_gif



def seach_command(ids: list, comments: list) -> list[str]:
    
    frames = []

    for id, message in zip(ids, comments):
        
        episodio = ''
        frame = ''
        captions =  ''
        
        if ('!dl' in message) and ('-e' in message) and ('-f' in message):  #!dl  -e 1 -f 1000 -t "Me happy"'
            
            numeros = re.findall(r'\d+', message) 
            
            if len(numeros) == 2:
                
                episodio = numeros[0]
                frame = f'frame_{numeros[1]}.jpg'
                
                if '-t' in message:
                    result = re.findall(r'"(.*?)"', message)
                    captions = ' '.join(result)

                frames.append([episodio, frame, captions, id])
        
        
        if message.startswith('!dl -h'):

            link_gif = get_random_frieren_gif(tag='Frieren anime')
            
            message = (
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
            f"{link_gif}"
            )

            help(id, message)
            
        if message.startswith('!gif'):
            
            tag = re.findall(r'"(.*?)"', message)
            if tag == []:
                tag = 'Frieren anime'
            
            link_gif = get_random_frieren_gif(tag)
            
            message = (
                f'random gif about {tag} :\n'
                f'{link_gif}'
                )
            
            help(id, message) 
                
                              
    return frames