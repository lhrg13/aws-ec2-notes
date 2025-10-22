# 🚀 Desafio DIO: Automatizando Workflows com AWS Step Functions

Este repositório é o entregável do desafio de consolidação de **Workflows Automatizados com AWS Step Functions** da Digital Innovation One (DIO). O objetivo principal foi aplicar os conceitos de orquestração de serviços *serverless* para construir um fluxo de trabalho resiliente e escalável na AWS.

## 🎯 Objetivos de Aprendizagem e Entrega

Com a conclusão deste desafio, demonstrei a capacidade de:

1.  Aplicar os conceitos de AWS Step Functions em um ambiente prático.
2.  Documentar processos técnicos de forma clara e estruturada.
3.  Utilizar o GitHub como ferramenta para compartilhamento de documentação técnica.

---

## 🛠️ O Workflow Construído

### Cenário de Uso: `<Descreva o cenário do seu State Machine, ex: Processamento Assíncrono de Pedido>`

O *State Machine* construído simula o fluxo de trabalho de `<Explicação breve do fluxo, ex: validação de dados, processamento principal e notificação/tratamento de erro, etc.>`

### ⚙️ Tecnologias Utilizadas

* **AWS Step Functions:** Serviço de orquestração central.
* **AWS Lambda:** Utilizado como `Task State` para simular as etapas de processamento.
* **AWS IAM:** Gerenciamento de permissões (Role do Step Functions).
* **Workflow Studio:** Ferramenta visual de design de workflow.

### Diagrama da Máquina de Estado

![Diagrama do Workflow](images/diagrama_step_functions.png)
*Detalhes:* O diagrama acima ilustra a sequência de estados e a lógica condicional implementada no Step Functions.

### Estrutura Detalhada do Workflow

| Estado (State) | Tipo | Função | Integração |
| :--- | :--- | :--- | :--- |
| **`<Nome do 1º Estado>`** | `Task` | `<Ex: Valida o input de entrada e garante que o payload é válido.>` | Lambda: `<Nome da Lambda de Validação>` |
| **`<Nome do 2º Estado (Se for Choice)>`** | `Choice` | `<Ex: Verifica se o campo 'status' é 'APROVADO' ou 'PENDENTE'.>` |
