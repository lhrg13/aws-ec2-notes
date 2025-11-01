# *Implementando Minha Primeira Stack com AWS CloudFormation*
Este repositório documenta o desafio prático de implementar uma Stack básica na AWS utilizando o serviço CloudFormation (Infraestrutura como Código - IaC), conforme proposto pela DIO.

---

## 🚩 Objetivo da Stack
Praticar o uso do AWS CloudFormation para criar e gerenciar um Bucket S3.
O desafio cobriu o ciclo de vida completo da IaC (Infraestrutura como Código):
* Escrever um template YAML válido.
* Criar a Stack (deploy).
* Verificar o bucket criado no S3.
* Excluir a Stack para limpar os recursos.

---

## AWS CloudFormantion
 O AWS CloudFormation é um serviço essencial da Amazon Web Services (AWS) que permite modelar e provisionar os seus recursos de infraestrutura AWS de forma automatizada e repetível.
 - **Infraestrutura como Código (IaC):** Permite que você defina toda a sua infraestrutura AWS, como instâncias EC2, bancos de dados RDS, redes VPC e etc, em um arquivo de texto (template).
 - **Templates (modelos):** Esses templates são escritos nos formatos JSON ou YAML e funcionam como um projeto para toda a sua configuração de infraestrutura.
 - **Automação:** O CloudFormation utiliza o template para implantar os recursos descritos, tratando a ordem de criação e todas as dependências entre eles automaticamente.
 - **Gerenciamento por Pilhas (Stacks):** Cada ambiente criado a partir de um template é chamado de Pilha (Stack), representando um conjunto harmônico de recursos que é gerenciado como uma única unidade (criação, atualização e exclusão coordenadas).
 - **Reutilização e Controle:** Os templates são reutilizáveis, garantindo a implantação de ambientes idênticos e consistentes (como desenvolvimento, staging e produção). Ao tratar a infraestrutura como código, é possível versionar esses templates (via Git), aplicando práticas de desenvolvimento de software como revisões de código e rollbacks.
 - **Cobrança:** O serviço CloudFormation em si não tem custo adicional.A cobrança é aplicada apenas pelos recursos da AWS que são provisionados e permanecem em uso (EC2, S3, etc.).

## 📒 Conceitos Relacionados
- **Templates (modelos):** Os arquivos JSON/YAML que definem os recursos.
- **Pilhas (Stacks):** A instância do seu modelo em execução na AWS, todos os recursos definidos no modelo são provisionados dentro da pilha.
- **Conjuntos de Alterações (Change Sets):** Uma visualização das alterações propostas que o CloudFormation fará nos recursos em execução antes da atualização.
- **AWS CDK (Cloud Development Kit):** Uma estrutura que permite definir a infraestrutura usando linguagens de programação familiares (Python, TypeScript, etc.), resumindo o resultado em modelos CloudFormation padrão.

---
## Processo de Implementação e Verificação
O processo seguiu os seguintes passos dentro do console da AWS:
1. Criação da Stack: Navegação até o serviço CloudFormation e upload do template.
2. Status da Criação: Acompanhamento da criação na aba "Eventos" até o status CREATE_COMPLETE.
3. Verificação (Outputs): Na aba "Saídas" da Stack, foi possível verificar o nome exato do bucket criado.
4. Verificação (S3): Ao navegar para o console do S3, o bucket estava listado e acessível.
5. Exclusão (Cleanup): O ciclo foi finalizado com a exclusão da Stack, que por sua vez, removeu automaticamente o bucket S3, demonstrando o poder do gerenciamento de ciclo de vida da IaC.

---
## 📌 Aprendizados
- O mais interessante foi ver a automação na prática: ao excluir a Stack, o CloudFormation deletou o bucket S3 sozinho.
- Aprendi que usar a variável ${AWS::AccountId} no nome do bucket é a forma correta de evitar erros de "nome duplicado.
- A aba "Saídas" (Outputs) é muito útil, pois mostra o resultado final, como o nome exato do bucket que foi criado.

---
## 📂 Arquivos do Repositório
* README.md: Esta documentação.
* /template.yaml: O template do CloudFormation utilizado para criar a stack.
* /images/: Pasta contendo os screenshots do processo.

