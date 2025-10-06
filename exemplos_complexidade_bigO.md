# Exemplos de Complexidades Big O

## O(log n) - Tempo Logarítmico
**Exemplo:** Procurar uma palavra no dicionário
- Você não procura palavra por palavra
- Abre no meio, vê se a palavra procurada vem antes ou depois
- Repete com a metade correta até encontrar
- Mesmo que o dicionário tenha 100.000 palavras, encontra em cerca de 17 etapas

## O(n) - Tempo Linear
**Exemplo:** Procurar um livro específico em uma pilha desorganizada
- Você precisa olhar livro por livro
- Se tiver 100 livros, no pior caso olha 100 livros
- Se tiver 1.000 livros, no pior caso olha 1.000 livros
- O tempo é proporcional ao número de livros

## O(n log n) - Tempo Linearítmico
**Exemplo:** Organizar uma coleção de cartas de baralho de forma eficiente
- Divide as cartas em grupos menores, ordena cada grupo, depois combina
- Mais rápido que métodos simples, mas não instantâneo
- Usado em algoritmos de ordenação eficientes como Merge Sort e QuickSort

## O(n²) - Tempo Quadrático
**Exemplo:** Comparar todas as pessoas em uma sala para encontrar duplicatas
- Cada pessoa compara com todas as outras
- Em uma sala com 10 pessoas: 10 × 10 = 100 comparações
- Em uma sala com 100 pessoas: 100 × 100 = 10.000 comparações
- O tempo cresce muito rapidamente

## O(n!) - Tempo Fatorial
**Exemplo:** O problema do caixeiro-viajante
- Um vendedor quer visitar 5 cidades na ordem mais curta possível
- Precisa testar todas as sequências possíveis: 5! = 120 rotas
- Para 10 cidades: 10! = 3.628.800 rotas
- Para 15 cidades: mais de 1 trilhão de rotas
- Torna-se impraticável muito rapidamente

## Analogia com transporte:
- O(log n): Pegar um avião (rápido, pouco afetado pela distância)
- O(n): Dirigir um carro (tempo proporcional à distância)
- O(n log n): Ônibus com paradas estratégicas
- O(n²): Andar a pé fazendo zigue-zague
- O(n!): Tentar todos os caminhos possíveis antes de chegar