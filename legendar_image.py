import subprocess


def legendar_image(frame, captions):


    if captions != '':
        
        partes = captions.split(' ')
        if len(partes) <= 5:
            backgound_size = '0x150' 
            
        elif len(partes) <= 10:
            partes.insert(5, '\n')
            captions = ' '.join(partes)
            backgound_size = '0x280'
        
        elif len(partes) <= 15:  
            partes.insert(5, '\n')
            partes.insert(10, '\n')
            captions = ' '.join(partes)
            backgound_size = '0x340'
            
        
        path_dir = './images/'
        gravity = '-gravity North'
        font =   '-font Cooper-Black'                        #'-font DejaVu-Sans-Bold' for linux
        font_size = '-pointsize 100'                         # '-font Arial-Bold' for windows
        backgound_color = '-background White'
        splice = f'-splice {backgound_size}'
        annotate = '-annotate +0+20'
        output_name = f'./images/s{frame}'
        
        subprocess.run(f'magick {path_dir}{frame} {gravity} {backgound_color} {splice} {font} {font_size} {annotate} "{captions}" {output_name}')
                        #magick for windows