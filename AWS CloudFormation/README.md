# Implementando Minha Primeira Stack com AWS CloudFormation
Este repositório documenta o desafio prático de implementar uma Stack básica na AWS utilizando o serviço CloudFormation (Infraestrutura como Código - IaC), conforme proposto pela DIO.

---

## 🚩 Objetivo da Stack

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
## 📂 Arquivos do Repositório

