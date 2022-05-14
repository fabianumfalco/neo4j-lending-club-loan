# Conjuntos de Dados (Datasets)

Os conjuntos de dados compreendem de empréstimos aceitos e rejeitados pelo Lending Club (LC) entre o período de 2007 a 2020.

LendingClub é uma empresa americana de empréstimos peer-to-peer (em português, par-a-par, ou simplesmente ponto a ponto) ou  empréstimos entre pessoas, com sede em San Francisco, Califórnia. Foi o primeiro credor peer-to-peer a registrar suas ofertas como valores mobiliários na Securities and Exchange Commission (SEC) e a oferecer negociação de empréstimos em um mercado secundário. LendingClub é a maior plataforma de empréstimos peer-to-peer do mundo. A empresa alega que US$ 15,98 bilhões em empréstimos foram originados por meio de sua plataforma até 31 de dezembro de 2015.

Os conjuntos de dados (4.88 GB) foram disponibilizados de forma pública em [Kaggle Datasets](https://www.kaggle.com/code/faressayah/lending-club-loan-defaulters-prediction/data):

# Dados Qualitativos (Soft Information)

Apenas os dados qualitativos (soft) foram considerados neste projeto.

Para extrair estes tipos de dados, foi criado o script pyhton  [extract_soft_information.py](https://github.com/fabianumfalco/neo4j-lending-club-loan/blob/main/data/extract_soft_information.py). Exemplo abaixo de uso desse script:

 <code>python extract_soft_information.py -i classe.um.csv -o classe.um.soft.csv</code>

Alguns estudos sugerem que a coleta e análise de dados qualitativos (soft/suaves) de mutuários sobre assuntos como família, amizades e outras questões pessoais e difíceis de conferir de forma quantitativa ajudam a reduzir as probabilidades de inadimplência de empréstimos.

Campo   | Descrição
--------- | ------
addr_state | O estado dos Estados Unidos fornecido pelo mutuário no pedido de empréstimo
annual_inc | A renda anual autodeclarada fornecida pelo mutuário durante o registro.
emp_length | Tempo de trabalho em anos. Os valores possíveis estão entre 0 e 10, onde 0 significa menos de um ano e 10 significa dez ou mais anos.
home_ownership | O status de propriedade da casa fornecido pelo mutuário durante o registro. Nossos valores são: RENT (ALUGUEL), OWN (PRÓPRIO), MORTGAGE (HIPOTECA), OTHER (OUTROS).
verification_status | Indica se a renda foi verificada por LC, se não foi verificada, ou se a fonte de renda foi verificada
loan_status | Situação atual do empréstimo

# Grafo no neo4j

O arquivo [node-similarity-classe.um.txt](https://github.com/fabianumfalco/neo4j-lending-club-loan/blob/main/dados/node-similarity-classe.um.txt) apresenta os comandos Cypher para criação do Grafo e sua projeção.
