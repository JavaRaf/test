



def carregar(ids_to_check):
    try:
        with open('responded_ids.txt', 'r') as file:
            # Ler todos os IDs do arquivo e remover espaços em branco e novas linhas
            ids_in_file = {line.strip() for line in file.readlines()}

        # Identificar os IDs que não estão no arquivo
        ids_not_in_file = [id for id in ids_to_check if id not in ids_in_file]

        return ids_not_in_file
    except FileNotFoundError:
        with open('responded_ids.txt', 'w'):
            print('criando o arquivo responded_ids.txt')
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def save_ids_to_txt(ids):
    try:
        with open('responded_ids.txt', 'a') as file:
            for id in ids:
                file.write(f"{id}\n")
        print(f"IDs salvos em responded_ids")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os IDs: {e}")