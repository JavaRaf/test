



def carregar(ids_to_check, comments_to_check):
    try:
        with open('responded_ids.txt', 'r') as file:
            # Ler todos os IDs do arquivo e remover espaços em branco e novas linhas
            ids_in_file = {line.strip() for line in file.readlines()}

        # Identificar os IDs que não estão no arquivo
        ids_not_in_file = []
        comments_not_in_file = []
        
        if ids_to_check and comments_to_check:
            for ids, comments in zip(ids_to_check, comments_to_check):
                if ids not in ids_in_file:
                    ids_not_in_file.append(ids)
                    comments_not_in_file.append(comments)
                       
            return ids_not_in_file, comments_not_in_file
    
    except FileNotFoundError:
        with open('responded_ids.txt', 'w'):
            print('criando o arquivo responded_ids.txt')
        
        return []
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def save_ids_to_txt(id_comentario):
    try:
        with open('responded_ids.txt', 'a') as file:
            file.write(f"{id_comentario}\n")
        print(f"id salvo em responded_ids")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o id: {e}")