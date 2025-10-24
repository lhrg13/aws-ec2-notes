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
<img width="665" height="516" alt="stepfunctions_graph" src="https://github.com/user-attachments/assets/e0c28ec0-93eb-4b9f-8b27-689e9aa8d8c8" />


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

### 1. Orquestração vs. Coreografia (Conceitual)
* **Insight:** O Step Functions permitiu uma **orquestração** clara, onde a lógica de negócio (o `Choice State`) é visível e centralizada, facilitando a auditoria de cada decisão.

### 2. Desafio de Permissão (IAM Role Scoped)
* **A Falha:** A execução inicial falhava no estado `Invoca Notificacao` devido a um `Access Denied` silencioso.
* **A Causa:** A Role de Execução do Step Functions (`StepFunctions-ValidaDados-role-...`) possuía uma política de permissão de escopo (`Scoped`) que **não listava o ARN** da `NotificaProcessoLambda`.
* **A Solução:** Foi necessário **editar o JSON da política de IAM** para incluir o ARN da `NotificaProcessoLambda` na lista de recursos permitidos para a ação `lambda:InvokeFunction`.

### 3. Desafio Crítico de Runtime (Node.js ESM vs. CommonJS)
* **A Falha Persistente:** Mesmo após corrigir o IAM, o erro **`ReferenceError: exports is not defined in ES module scope`** persistiu nos logs do CloudWatch.
* **A Causa:** O código da `NotificaProcessoLambda` estava escrito em sintaxe **CommonJS (CJS)** (`exports.handler`), mas o runtime **Node.js 22.x** estava configurado para esperar o formato **Módulo ES (ESM)**.
* **A Solução:** O código da Lambda foi alterado para a sintaxe **Módulo ES (ESM)**, usando `export const handler = async (event) => {...}`. Isso resolveu o erro de inicialização do runtime e garantiu o sucesso da execução.

### 4. Resiliência e Tratamento de Erros
* O bloco `Catch` foi testado com sucesso: ao forçar uma falha na Lambda, o Step Functions capturou o erro (`TaskFailed`) e desviou o fluxo para o `Notificacao Falhou`, provando a robustez do design.

---

## 📂 Organização do Repositório

* `/images`: Contém a captura de tela do diagrama e da execução bem-sucedida.
* `/state-machine-definition`: Contém o arquivo JSON com a definição completa da Máquina de Estado em ASL.
* *Outras pastas podem ser adicionadas para o código Lambda, se desejado.*

---

## 🔗 Recursos e Documentação

* [AWS Step Functions - Documentação Oficial](https://aws.amazon.com/pt/step-functions/)
* [Especificação da Linguagem Amazon States (ASL)](https://states-language.net/spec.html)
* [Digital Innovation One - Plataforma de Aprendizagem](https://www.dio.me/)

---
*Feito com 💜 e depurado no detalhe por: [Seu Nome Completo]*
