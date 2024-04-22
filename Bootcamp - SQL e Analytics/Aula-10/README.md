## Transação

### O que é uma transação?

- Uma coleção de "queries"
- Uma unidade de trabalho
Muitas vezes precisamos mais de uma "querie" para querer o que queremos
ex: para fazer uma transação financeira, precisamos selecionar uma conta e verificar se ela possui o dnheiro (SELECT), fazer a remoção do dinheiro da conta que irá transferir o dinheiro (UPDATE) e fazer o incremento do dinheiro na conta alvo (UPDATE). Tudo isso precisa estar dentro da mesma transação.
- Toda transação inicia com um BEGIN
- Toda transação finaliza com um COMMIT (em memória)
- Toda transação, pode falhar, precisa de um ROLLBACK 
- Normalmente transações são usadas para MODIFICAR dados, mas é possível ter uma transação com somente leitura , exemplo: você quer gerar um relatório e quer que esses dados sejam confiáveis e ter uma SNAPSHOT daquela cenário

## Atomicidade

- Uma transação tem que ser "indivisivel"
- Ou seja, todas as "queries" em uma transação precisam ter sucesso
- Exemplo: se não existir a segunda pessoa, se você não tiver 100 reais, se cair a luz no meio dessa transação, etc. Ela volta para o estado anterior e nada acontece.
