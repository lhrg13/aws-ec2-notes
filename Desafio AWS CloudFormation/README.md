# Implementando um Servidor EC2 com AWS CloudFormation
Este repositório documenta o desafio prático de implementar uma Stack na AWS que provisiona um Servidor EC2 e um Grupo de Segurança (Security Group) utilizando o CloudFormation (Infraestrutura como Código - IaC).

# 🚩 Objetivo da Stack

Praticar o uso do AWS CloudFormation para provisionar um recurso computacional (EC2) e sua dependência de rede (Security Group). O desafio cobriu o ciclo de vida completo da IaC:
* Escrever um modelo YAML válido com múltiplos recursos.
* Cria uma chave SHH.
* Criar a Pilha.
* Verifique o EC2 criado.
* Exclua uma pilha para limpar os recursos.

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
1. Pré-requisito: Criação manual da Chave SSH (Key Pair) minha-chave-aws no console do EC2.
2. Criação: Upload do template no CloudFormation e lançamento da Stack (ex: dio-servidor-dev).
3. Verificação (Outputs): Na aba "Saídas" da Stack, foram confirmados o InstanceID e o PublicIP da nova instância.
4. Verificação (Console): No console do EC2, a instância meu-servidor-cfn foi confirmada como "Em execução" (Running).
5. Exclusão (Cleanup): A exclusão da Stack no CloudFormation removeu automaticamente tanto a Instância EC2 quanto o Security Group associado.

---
## 📌 Aprendizados
- O mais interessante foi ver o CloudFormation gerenciar a ordem: ao criar a Stack, ele fez o Security Group antes da Instância EC2. Ao excluir, ele removeu a Instância antes do Security Group.
- Aprendi que !Ref é a "cola" entre os recursos. Usei !Ref MeuSecurityGroup para injetar o ID do firewall na configuração da instância, garantindo que eles estivessem conectados.
- No caso do EC2, a aba "Saídas" é ainda mais importante. Ela é essencial para descobrir o PublicIP (IP Público) do servidor, que é dinâmico e só é conhecido após a criação.
- !Ref MinhaInstanciaEC2 me daria o ID da instância (ex: i-12345).
- !GetAtt MinhaInstanciaEC2.PublicIp me deu um atributo específico (o IP público).

---
## 📂 Arquivos do Repositório
* README.md: Esta documentação.
* /ec2-com-chave-fixa-template.yaml: O template do CloudFormation utilizado para criar a pilha EC2.
* /images/: Pasta contendo as capturas de tela do processo (stack, console EC2, aba de saídas).

