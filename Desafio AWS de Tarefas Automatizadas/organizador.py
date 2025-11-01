
import boto3
import os
import urllib.parse

# Cria um cliente S3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    # 1. Obter o nome do bucket e a chave (nome do arquivo) do evento
    record = event['Records'][0]
    source_bucket = record['s3']['bucket']['name']
    
    # Decodifica a chave do arquivo (em caso de caracteres especiais)
    file_key = urllib.parse.unquote_plus(record['s3']['object']['key'])
    
    print(f"Novo arquivo detectado: {file_key} no bucket {source_bucket}")

    # Verifica se o arquivo já está em uma pasta
    if '/' in file_key:
        print(f"O arquivo '{file_key}' já está em uma pasta. Ignorando.")
        return

    # 2. Determina o tipo do arquivo com base na extensão
    _, file_extension = os.path.splitext(file_key)
    file_extension = file_extension.lower() 

    if file_extension in ['.png', '.jpg', '.jpeg', '.gif']:
        target_folder = 'imagens'
    elif file_extension in ['.pdf', '.doc', '.docx', '.txt']:
        target_folder = 'documentos'
    elif file_extension in ['.zip', '.rar', '.gz']:
        target_folder = 'compactados'
    else:
        target_folder = 'outros'
        
    target_key = f"{target_folder}/{file_key}"
    
    print(f"Movendo '{file_key}' para '{target_key}'...")

    try:
        # 3. Copiar o objeto para a nova localização
        copy_source = {'Bucket': source_bucket, 'Key': file_key}
        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=source_bucket,
            Key=target_key
        )
        
        # 4. Deletar o objeto original
        s3_client.delete_object(
            Bucket=source_bucket,
            Key=file_key
        )
        
        print("Arquivo movido com sucesso!")
        
    except Exception as e:
        print(f"Erro ao mover arquivo: {str(e)}")
        raise e
