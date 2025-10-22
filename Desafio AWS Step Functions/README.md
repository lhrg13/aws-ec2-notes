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
| **`<Nome do 2º Estado (Se for Choice)>`** | `Choice` | `<Ex: Verifica se o campo 'status' é 'APROVADO' ou 'PENDENTE'.>` | Lógica Condicional |
| **`<Caminho A>`** | `Parallel` / `Task` | `<Ex: Se APROVADO, inicia o processamento do pagamento e a preparação do envio em paralelo.>` | Lambda / Outro Serviço |
| **`<Caminho B>`** | `Fail` / `Succeed` | `<Ex: Se PENDENTE, falha a execução com um erro específico ou notifica o usuário.>` | |
| **`<Estado Final>`** | `Succeed` | Encerra a execução com sucesso. | |

---

## 💡 Anotações e Insights Adquiridos (Step Functions Aprofundado)

A prática neste desafio reforçou a compreensão dos conceitos-chave de orquestração de serviços.

### 1. Orquestração vs. Coreografia

* **Step Functions (Orquestração):** O controle centralizado (o *State Machine*) dita a sequência e o estado de todo o processo. Ideal para fluxos de missão crítica onde a auditoria e a ordem são essenciais.
* **Coreografia (SNS/SQS):** Os serviços interagem e se comunicam de forma autônoma através de eventos (mensagens). Menos controle, mas mais flexibilidade.
* **Insight:** O Step Functions permite construir processos **resilientes** e **visuais** de forma que seria complexo e propenso a erros utilizando apenas filas e tópicos.

### 2. Manipulação de Dados (Input/Output Processing)

A passagem de dados entre os estados é crucial e foi gerenciada utilizando:

* **`InputPath`:** Garante que apenas a seção relevante do JSON de entrada seja enviada ao estado.
* **`ResultPath`:** Define como o resultado (`Result`) de uma `Task` (ex: a resposta de uma Lambda) é fundido de volta ao JSON de execução. Utilizei `"ResultPath": "$.processamento_output"` para não sobrescrever os dados originais.
* **`OutputPath`:** Filtra o JSON final de saída do estado, garantindo um payload limpo para o próximo estado.

### 3. Resiliência e Tratamento de Erros

A robustez do fluxo foi garantida através das seguintes configurações no **`Task State`**:

* **Retries (Tentativas Automáticas):**
    * Configurado para tentar novamente em caso de erros temporários (`ErrorEquals`: ["Lambda.UnknownError"], `MaxAttempts`: 3, `BackoffRate`: 2).
    * Isso evita falhas desnecessárias devido a falhas transientes de rede ou sobrecarga.
* **Catchers (Captura de Erros):**
    * Em caso de falha persistente após as tentativas, o `Task` transiciona para um `Catch` que redireciona o fluxo para um estado de **Notificação de Erro**, impedindo que toda a execução falhe abruptamente.

### 4. O Uso do `Choice State`

O `Choice State` foi vital para implementar a lógica de negócio **`Se/Senão (If/Else)`**. Ele opera avaliando regras como `NumericGreaterThan`, `StringEquals` ou `IsPresent` sobre os dados de entrada, direcionando a execução para caminhos diferentes do workflow.

---

## 📂 Organização do Repositório

* **`/images`:** Contém as capturas de tela relevantes da AWS Console (Diagrama, Execução Sucedida, Logs).
* **`/state-machine-definition`:** Contém o arquivo JSON/YAML com a definição completa da Máquina de Estado em ASL (Amazon States Language).
* **`/lambda-functions`:** Contém o código (opcional) das funções Lambda utilizadas no workflow.

## 🔗 Recursos e Documentação

* [AWS Step Functions - Documentação Oficial](https://aws.amazon.com/pt/step-functions/)
* [Amazon States Language (ASL) Specification](https://states-language.net/spec.html)
* [Digital Innovation One - Plataforma de Aprendizagem](https://www.dio.me/)

### **Como Executar Este Projeto:**

1.  Crie as funções Lambda necessárias na sua conta AWS.
2.  Copie e cole o código ASL da pasta `/state-machine-definition` no console do AWS Step Functions.
3.  Ajuste os ARNs das funções Lambda no código ASL para corresponderem aos seus recursos.
4.  Execute a Máquina de Estado e monitore a execução no painel visual!

