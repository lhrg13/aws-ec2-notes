# Desafio DIO: Automação S3 e Lambda com LocalStack
Este repositório documenta a implementação de uma automação *serverless* com S3 e Lambda, como parte do desafio da DIO. O projeto utiliza o **LocalStack** para simular a infraestrutura AWS localmente, permitindo testes rápidos e sem custo.

---

### 🚩 Objetivo do Projeto
Praticar o uso combinado do Amazon S3 e AWS Lambda para criar um fluxo de trabalho orientado a eventos.

* Escrever uma função Lambda em Python para organizar arquivos.
* Criar um bucket S3 para armazenamento.
* Configurar um trigger (gatilho) no S3 para acionar a Lambda em novos uploads.
* Implementar a lógica da Lambda para mover arquivos para pastas específicas.
* Testar a automação fazendo upload de arquivos.
* Verificar o resultado (arquivos movidos).
* Utilizar o LocalStack para simular os serviços AWS localmente.

---

### Amazon S3 (Simple Storage Service)
O Amazon S3 é um serviço de armazenamento de objetos em nuvem. Neste projeto, foi usado para armazenar os arquivos. Configurei o S3 para acionar a Lambda automaticamente sempre que um novo arquivo fosse enviado.

### AWS Lambda
O AWS Lambda é um serviço de computação *serverless* que executa código em resposta a eventos, sem a necessidade de gerenciar servidores. 
Foi usada para executar o código Python. Assim que era acionada pelo S3, a Lambda analisava a extensão do arquivo (como .png ou .txt) e movia o arquivo para a pasta correta (como imagens/ ou documentos/).

---

## 📒 Conceitos Relacionados

* **LocalStack:** A ferramenta essencial que me permitiu simular o S3 e o Lambda na minha máquina (`localhost:4566`).
* **Triggers (Gatilhos):** A configuração que "conecta" o S3 à Lambda, dizendo quando ela deve ser acionada.
* **Arquitetura Orientada a Eventos (EDA):** O padrão que usamos. Os serviços não se chamam diretamente, eles apenas reagem a eventos (como um upload de arquivo).
* **IAM Role (Fictícia):** Um ARN "dummy" (...:role/lambda-role) usado no LocalStack para simular as permissões de segurança que a AWS real exigiria.

---

## Processo de Implementação e Verificação

O processo seguiu os seguintes passos no terminal (PowerShell) com o LocalStack em execução:
1.  **Criação (S3):** Criação do *bucket* "meu-bucket-organizador" via AWS CLI.
2.  **Criação (Lambda):** ECriação da função "OrganizadorDeArquivos" a partir do pacote .zip.
3.  **Permissão:** Execução do "aws lambda add-permission" para permitir que o S3 invoque a Lambda.
4.  **Gatilho (Trigger):** Aplicação da notificação (put-bucket-notification-configuration) no bucket S3 para conecta-lo à função.
5.  **Teste (Upload):** Envio de arquivos de teste (como relatorio.txt e foto.png) para a raiz do bucket.
6.  **Resultado (S3):** Verificação com aws s3 ls --recursive, que confirmou os arquivos movidos para suas pastas de destino (ex: documentos/).
7.  **Logs (Docker):** Inspeção dos logs (docker logs localstack-main) para confirmar as chamadas de API (CopyObject, DeleteObject) executadas pela Lambda.

---

## 📌 Aprendizados

* Para evitar um loop, eu adicionei uma verificação. A Lambda ignora arquivos que já estão na pasta, assim ela não é acionada de novo pelo seu próprio movimento.
* "Mover" no S3 não é um comando único. A Lambda precisou, na verdade, Copiar o arquivo para o novo local e, em seguida, Apagar o arquivo original.
* O LocalStack tornou tudo mais rápido. Ele permitiu testar o fluxo sem precisar configurar permissões (IAM) complexas.
* O evento do S3 é completo. Ele já informa à Lambda qual arquivo foi enviado e onde ele está, então o código pode focar apenas em movê-lo.
---

## 📂 Arquivos do Repositório

* **README.md**: Esta documentação.
* **/organizador.py**: O código-fonte Python da função Lambda.
* **/notification.json**: Arquivo de configuração do gatilho do S3.
* **/images/**: Capturas de tela do processo (criação, upload, resultado e logs).
