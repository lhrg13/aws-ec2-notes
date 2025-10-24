# 🚀 Desafio DIO: Automatizando Workflows com AWS Step Functions

Este repositório é o entregável do desafio de consolidação de **Workflows Automatizados com AWS Step Functions** da Digital Innovation One (DIO). O objetivo principal foi aplicar os conceitos de orquestração de serviços *serverless* para construir um fluxo de trabalho resiliente e escalável na AWS.

### Status do Projeto
✅ **Concluído e Testado com Sucesso após Depuração**

---

## 🎯 Objetivos de Aprendizagem e Entrega

Com a conclusão deste desafio, demonstrei a capacidade de:
1.  Aplicar os conceitos do AWS Step Functions em um ambiente prático.
2.  Documentar processos técnicos de forma clara e estruturada.
3.  Utilizar o GitHub como ferramenta para compartilhamento de documentação técnica.

---

## 📚 Conceitos Fundamentais de Arquitetura

O AWS Step Functions é essencial para orquestrar serviços que operam em arquiteturas de **microsserviços** e **serverless**.

### 🔹 AWS Lambda (Computação Serverless)
* **Definição:** Serviço de computação *serverless* que executa seu código em resposta a eventos e gerencia automaticamente toda a infraestrutura subjacente (servidores, escalabilidade, SO).
* **Vantagens:** Cobrança por uso (`Pay-per-use`) e escalabilidade automática, permitindo foco total no código.

### 🔹 Microsserviços e Desacoplamento
* **Microsserviços:** Arquitetura que estrutura uma aplicação como uma coleção de serviços pequenos e **autônomos**, cada um focado em uma funcionalidade de negócio específica.
* **Desacoplamento (*Loose Coupling*):** O princípio mais importante. Significa que os serviços são independentes. Uma falha em um serviço não derruba a aplicação inteira, aumentando a **resiliência** do sistema.
* **Relação com Step Functions:** Step Functions é a ferramenta ideal para **orquestrar** esses microsserviços, garantindo que eles sejam chamados na ordem correta e que as falhas sejam tratadas de forma elegante.

### 🔹 Serviços de Contêineres (ECS/EKS)
* **Amazon ECS / EKS:** Serviços de orquestração utilizados para executar microsserviços empacotados em contêineres.
    * **ECS (Elastic Container Service):** Orquestrador nativo da AWS, simples para gerenciar contêineres.
    * **EKS (Elastic Kubernetes Service):** Serviço gerenciado para executar clusters Kubernetes na AWS, ideal para arquiteturas complexas ou equipes familiarizadas com o K8s.

---

## 🛠️ O Workflow Construído

### Cenário de Uso: Processamento Condicional de Dados

A **Máquina de Estado** construída simula um fluxo de trabalho de **processamento condicional**, onde a execução é ramificada com base em um valor de entrada:
* Se o valor de entrada é **maior ou igual a 10**, ele segue para uma notificação (indicando alto valor).
* Se o valor é **menor que 10**, ele segue o caminho padrão e encerra com sucesso (baixo valor).

### ⚙️ Tecnologias Utilizadas

* **AWS Step Functions:** Serviço de orquestração central.
* **AWS Lambda:** Utilizado como `Task State` para simular as etapas de processamento.
* **AWS IAM:** Gerenciamento de permissões (Role do Step Functions).
* **Workflow Studio:** Ferramenta visual de design de fluxo de trabalho.

### Diagrama da Máquina de Estado
<img width="665" height="516" alt="stepfunctions_graph" src="https://github.com/user-attachments/assets/9712d5ac-a766-4362-a04a-6b2acac5c820" />


### Estrutura Principal do Workflow

| Estado (State) | Tipo | Função | Integração |
| :--- | :--- | :--- | :--- |
| **Valida Dados (Pass)** | `Pass` | Prepara e passa o input para o próximo estado. | N/A |
| **Verifica Valor** | `Choice` | Verifica a condição `$.valor >= 10`. | Lógica Condicional |
| **Invoca Notificacao** | `Task` | É o caminho de alto valor. Invoca a função Lambda de notificação. | `Lambda: NotificaProcessoLambda` |
| **Notificacao Falhou** | `Fail` | É o caminho de erro (`Catch`) acionado se a Lambda falhar. | `Fail State` |
| **Processamento Baixo Concluido** | `Succeed` | É o caminho `Default` para baixo valor. Encerra a execução com sucesso. | `Succeed State` |
---


## 💡 Anotações e Insights Adquiridos (Depuração Avançada)

A prática neste desafio reforçou a compreensão dos conceitos-chave, especialmente na resolução de problemas de ambiente e permissão, que são críticos em projetos *serverless*.

### 1. Desafio de Permissão (IAM Role Scoped)
* **O Problema:** A execução falhava ao tentar chamar a `NotificaProcessoLambda`. O erro não era na máquina de estado, mas na sua **Role de Execução (IAM Role)**.
* **A Solução:** Foi necessário **editar o JSON da política de IAM** para adicionar o ARN da `NotificaProcessoLambda` ao array de recursos permitidos.

### 2. Desafio Crítico de Runtime (Node.js ESM vs CJS)
* **O Problema:** O erro persistente foi **`ReferenceError: exports is not defined in ES module scope`** (visto no CloudWatch).
* **A Causa:** O código da Lambda estava em sintaxe **CommonJS (CJS)** (`exports.handler`), mas o runtime **Node.js 22.x** estava configurado para esperar o formato **Módulo ES (ESM)**.
* **A Solução:** O código da Lambda foi alterado para a sintaxe **Módulo ES (ESM)** (`export const handler = async (event) => {...}`), resolvendo o erro de inicialização.

### 3. Validação do Tratamento de Erro (`Catch`)
* O bloco `Catch` foi testado com sucesso: a falha forçada na Lambda foi capturada, e o Step Functions desviou o fluxo corretamente para o `Fail state`, provando a **resiliência** do design.

---

## 📂 Organização do Repositório

* `/images`: Contém a captura de tela do diagrama e da execução bem-sucedida.
* `/state-machine-definition`: Contém o arquivo JSON com a definição completa da Máquina de Estado em ASL.

---

## 🔗 Recursos e Documentação

* [AWS Step Functions - Documentação Oficial](https://aws.amazon.com/pt/step-functions/)
* [Especificação da Linguagem Amazon States (ASL)](https://states-language.net/spec.html)
* [Digital Innovation One - Plataforma de Aprendizagem](https://www.dio.me/)
* https://docs.google.com/document/d/1-HiQhphNYBntMCZiYJY_EK_WW1CVHV5M1PWULj0lL5o/edit?tab=t.m9jrwo2fw5eo
