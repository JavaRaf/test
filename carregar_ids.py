


def carregar(ids_to_check, comments_to_check):
    if len(ids_to_check) != len(comments_to_check):
        print("A lista de IDs e a lista de comentários devem ter o mesmo comprimento.")
        return [], []
    
    try:
        with open('responded_ids.txt', 'r') as file:
            ids_in_file = {line.strip() for line in file.readlines()}

        ids_not_in_file = []
        comments_not_in_file = []
        
        for ids, comments in zip(ids_to_check, comments_to_check):
            if ids not in ids_in_file:
                ids_not_in_file.append(ids)
                comments_not_in_file.append(comments)
                       
        return ids_not_in_file, comments_not_in_file
    
    except FileNotFoundError:
        with open('responded_ids.txt', 'w') as file:
            print('criando o arquivo responded_ids.txt')
        
        return [], []
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return [], []

def save_ids_to_txt(id_comentario):
    try:
        with open('responded_ids.txt', 'a') as file:
            file.write(f"{id_comentario}\n")
        print(f"id salvo em responded_ids")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o id: {e}")
