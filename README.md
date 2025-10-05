# Desafio DIO: Gerenciando Instâncias EC2 e Armazenamento na AWS
Este repositório é minha entrega para o desafio da DIO sobre gerenciamento de instâncias EC2 e conceitos fundamentais de computação em nuvem. Ele consolida o conhecimento adquirido sobre a infraestrutura da AWS, serviços de computação e armazenamento, otimização de recursos e práticas de segurança.

---

### 💡 Conceitos Essenciais da AWS

A AWS (Amazon Web Services) oferece uma infraestrutura de nuvem **robusta**, de **alta escalabilidade** e **segura**. Compreender seus conceitos é crucial para qualquer projeto.

#### Modelos de Computação em Nuvem

Cada modelo oferece um nível diferente de controle e responsabilidade para o usuário:

* **SaaS (Software como Serviço):** **USE**. O serviço está pronto para uso. Exemplo: E-mail.
* **PaaS (Plataforma como Serviço):** **CONSTRUA**. O usuário implanta sua aplicação na plataforma. Exemplo: Ambientes de desenvolvimento.
* **IaaS (Infraestrutura como Serviço):** **MIGRE**. O usuário gerencia a infraestrutura, como máquinas virtuais. Exemplo: Servidores de arquivos.

#### Infraestrutura Global da AWS

A AWS opera com uma rede global de data centers para garantir alta disponibilidade e baixa latência.
* **Regions (Regiões):** Áreas geográficas isoladas com múltiplos data centers. Essenciais para tolerância a falhas.
* **Availability Zones (Zonas de Disponibilidade):** Data centers independentes dentro de uma região, conectados para alta disponibilidade. A replicação de dados entre regiões deve ser configurada manualmente.

#### Segurança e Acesso

* **IAM (Identity and Access Management):** Ferramenta para gerenciar acessos e permissões. É uma boa prática usar a conta **root** apenas para a configuração inicial e depois criar usuários com o **princípio do privilégio mínimo**.
* **MFA (Multi-Factor Authentication):** Uma camada de segurança extra que exige dois ou mais métodos de verificação para acessar a conta.

---

### 💻 Computação na Nuvem com EC2

O **Amazon EC2 (Elastic Compute Cloud)** é o serviço que fornece máquinas virtuais (`instâncias`) na nuvem da AWS, sendo um exemplo clássico de **IaaS**.

#### Tipos de Instâncias EC2

A escolha da instância correta é vital para a eficiência e o custo. As famílias de instâncias são otimizadas para diferentes cargas de trabalho:

* **Uso Geral (`T2`, `M4`):** Para aplicações e bancos de dados simples.
* **Otimizado para Computação (`C4`):** Para aplicativos intensivos em CPU.
* **Otimizado para Memória (`R4`, `X1`):** Para bancos de dados e aplicações que precisam de muita RAM.
* **Otimizado para Armazenamento (`I3`, `D2`):** Para bancos de dados NoSQL e Big Data.

<img width="960" height="540" alt="Tipos EC2" src="https://github.com/user-attachments/assets/229e56ec-d9a8-48b2-8fa4-70e74cf6bc91" />

#### Otimização e Escalabilidade

* **Otimização de Custos:**
    * **Desligar recursos ociosos:** Instâncias de desenvolvimento/teste podem ser desligadas fora do horário de trabalho.
* **Modelos de Compra:**
    * **Sob Demanda:** Flexível, pago por hora.
    * **Reservadas:** Desconto por compromisso de 1 ou 3 anos.
    * **SPOT:** Grandes descontos, mas a instância pode ser encerrada a qualquer momento pela AWS.
* **Escalabilidade (Scale):**
    * **Vertical:** Aumentar a capacidade de uma única instância (mais CPU/memória).
    * **Horizontal:** Aumentar o número de instâncias para distribuir a carga.

---

### 💾 Armazenamento na Nuvem: EBS e S3

A AWS oferece serviços de armazenamento para diferentes necessidades de performance, custo e durabilidade.

#### Amazon EBS (Elastic Block Store)

É um serviço de armazenamento em **bloco**, que funciona como um disco rígido virtual para instâncias EC2.

* **Uso Principal:** Volumes para sistemas de arquivos, bancos de dados (MySQL, PostgreSQL) e logs.
* **Snapshots do EBS:** São backups pontuais de volumes EBS, armazenados no Amazon S3. Essenciais para recuperação de desastres (DR) e criação de volumes.

#### Amazon S3 (Simple Storage Service)

É um serviço de armazenamento de **objetos** ideal para grandes volumes de dados de forma escalável e segura.

* **Classes de Armazenamento:**
    * **S3 Standard:** Para dados de acesso frequente.
    * **S3 Intelligent-Tiering:** Move dados entre as classes de forma automática para otimizar custos.
    * **S3 Glacier:** Para arquivamento de longo prazo, com custo muito baixo e tempo de recuperação mais longo.

* **Regras de Ciclo de Vida:** Permite automatizar a transição de objetos entre as classes, otimizando os custos de armazenamento ao longo do tempo.


<img width="881" height="735" alt="image" src="https://github.com/user-attachments/assets/ed6b9153-7ea7-4b21-916a-b11ecea5e01d" />


<img width="987" height="505" alt="image" src="https://github.com/user-attachments/assets/c3132ea4-e701-4ac9-ab5c-578cba7d19da" />

---

### 📝 Anotações: 
Fique à vontade para consultar minhas anotações sobre AWS:
https://docs.google.com/document/d/1-HiQhphNYBntMCZiYJY_EK_WW1CVHV5M1PWULj0lL5o/edit?usp=sharing

Fique à vontade para consultar minhas anotações sobre linguagens de programação:
https://docs.google.com/document/d/1U9DX4HWNCONbbbeXnt2XWKlF2bvth04ItrHQBfjLmZE/edit?usp=sharing


---

### 🖼️ Diagrama de Arquitetura

Como parte do desafio, criei um diagrama para visualizar a integração dos serviços AWS. A arquitetura conecta `S3`, `Lambda Function`, `EC2` e `EBS`, demonstrando a interação entre diferentes componentes para formar uma solução completa.

O diagrama foi criado utilizando a ferramenta [draw.io](https://www.draw.io/).

<img width="721" height="1075" alt="Diagrama Desafio Instâncias EC2" src="https://github.com/user-attachments/assets/8d11d741-3118-4a44-9b86-43e12a5011f4" />

---

### 🚀 Conclusão

Este desafio me permitiu consolidar a visão do ecossistema AWS, do nível de infraestrutura global até a gestão detalhada de recursos como EC2 e S3. A prática de documentar o processo me ajudou a fixar os conceitos e aprimorar minhas habilidades de comunicação técnica, elementos essenciais para qualquer profissional de nuvem.
