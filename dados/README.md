# Conjuntos de Dados (Datasets)

Os conjuntos de dados compreendem de empréstimos aceitos e rejeitados pelo Lending Club (LC) entre o período de 2007 a 2020.

LendingClub é uma empresa americana de empréstimos peer-to-peer (em português, par-a-par, ou simplesmente ponto a ponto) ou  empréstimos entre pessoas, com sede em San Francisco, Califórnia. Foi o primeiro credor peer-to-peer a registrar suas ofertas como valores mobiliários na Securities and Exchange Commission (SEC) e a oferecer negociação de empréstimos em um mercado secundário. LendingClub é a maior plataforma de empréstimos peer-to-peer do mundo. A empresa alega que US$ 15,98 bilhões em empréstimos foram originados por meio de sua plataforma até 31 de dezembro de 2015.

Os conjuntos de dados (4.88 GB) foram disponibilizados de forma pública em [Kaggle Datasets](https://www.kaggle.com/code/faressayah/lending-club-loan-defaulters-prediction/data):

# Dados Qualitativos (Soft Information)

Apenas os dados qualitativos (soft) foram considerados neste projeto.

Para extrair estes tipos de dados, foi criado o script pyhton abaixo [extract_soft_information.py](https://github.com/fabianumfalco/neo4j-lending-club-loan/blob/main/data/extract_soft_information.py)

Alguns estudos sugerem que a coleta e análise de dados qualitativos (soft/suaves) de mutuários sobre assuntos como família, amizades e outras questões pessoais e difíceis de conferir de forma quantitativa ajudam a reduzir as probabilidades de inadimplência de empréstimos.

Campo   | Descrição
--------- | ------
addr_state | O estado dos Estados Unidos fornecido pelo mutuário no pedido de empréstimo
annual_inc | A renda anual autodeclarada fornecida pelo mutuário durante o registro.
emp_length | Tempo de trabalho em anos. Os valores possíveis estão entre 0 e 10, onde 0 significa menos de um ano e 10 significa dez ou mais anos.
home_ownership | O status de propriedade da casa fornecido pelo mutuário durante o registro. Nossos valores são: RENT (ALUGUEL), OWN (PRÓPRIO), MORTGAGE (HIPOTECA), OTHER (OUTROS).
verification_status | Indica se a renda foi verificada por LC, se não foi verificada, ou se a fonte de renda foi verificada
loan_status | Situação atual do empréstimo

# Grafos no neo4j

Importar dados de arquivo CSV e criar nós dos mutuários (Borrower)

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (b:Borrower {borrowerId: row.borrower_id});`

Importar dados de arquivo CSV e criar nós dos estados dos Estados Unidos

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (s:State {stateCode: row.addr_state});`

Importar dados de arquivo CSV e criar nós das situações atuais dos empréstimos

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (l:LoanStatus {loanStatus: row.loan_status});`

Importar dados de arquivo CSV e criar nós das situações de propriedade da casa

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (h:HomeOwnership {homeOwnership: row.home_ownership});`

Importar dados de arquivo CSV e criar nós das rendas anuais autodeclaradas pelos mutuários

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (i:AnnualInc {annualInc: row.annual_inc});`

Importar dados de arquivo CSV e criar nós das situações de indicações de verificações de rendas anuais autodeclaradas

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (v:VerificationStatus {verificationStatus: row.verification_status});`

Importar dados de arquivo CSV e criar nós dos tempo de trabalho

`LOAD CSV WITH HEADERS FROM 'file:///Loan_status_2007-2020Q3_100_soft.csv' AS row
WITH row
MERGE (e:EmpLength {empLength: row.emp_length});`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e estados

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (s:State {stateCode: row.addr_state})
MERGE (b)-[:HAS_ADDRESS_IN]->(s)`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e situações de emprestimos

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (l:LoanStatus {loanStatus: row.loan_status})
MERGE (b)-[:HAS_STATUS_LOAN]->(l)`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e situações de propriedade de casa

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (h:HomeOwnership {homeOwnership: row.home_ownership})
MERGE (b)-[:HAS_HOME_OWNERSHIP]->(h)`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e rendas anuais autodeclaradas

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (i:AnnualInc {annualInc: row.annual_inc})
MERGE (b)-[:HAS_INCOME_ANNUAL]->(i)`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e situações de verificações de rendas anuais

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (v:VerificationStatus {verificationStatus: row.verification_status})
MERGE (b)-[:HAS_VERIFICATION_INCOME]->(v)`

Importar dados de arquivo CSV e criar relacionamentos entre os nós dos mutuários e tempo de trabalho

`WITH "file:///Loan_status_2007-2020Q3_100_soft.csv" AS uri
LOAD CSV WITH HEADERS FROM uri AS row
MATCH (b:Borrower {borrowerId: row.borrower_id})
MATCH (e:EmpLength {empLength: row.emp_length})
MERGE (b)-[:HAS_EMPLOYMENT_LENGTH]->(e)`
