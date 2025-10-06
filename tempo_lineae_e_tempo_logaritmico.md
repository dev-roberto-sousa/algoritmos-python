# Explicação sobre Tempo Linear e Tempo Logarítmico

## Tempo Linear (O(n))

**O que é:** O tempo de execução cresce proporcionalmente ao tamanho dos dados.

**Exemplo prático:** Procurar um nome em uma lista telefônica não ordenada.

- Se tiver 100 nomes: no pior caso, verifica 100 nomes
- Se tiver 1.000 nomes: no pior caso, verifica 1.000 nomes  
- Se tiver 10.000 nomes: no pior caso, verifica 10.000 nomes

**Característica:** Se você dobra o tamanho dos dados, dobra o tempo de execução.

## Tempo Logarítmico (O(log n))

**O que é:** O tempo de execução cresce muito lentamente mesmo com dados muito grandes.

**Exemplo prático:** Procurar um nome em uma lista telefônica ordenada (busca binária).

- Se tiver 100 nomes: no pior caso, verifica 7 nomes
- Se tiver 1.000 nomes: no pior caso, verifica 10 nomes
- Se tiver 1.000.000 nomes: no pior caso, verifica 20 nomes

**Característica:** Se você dobra o tamanho dos dados, o tempo aumenta apenas um pouco.

## Comparação Direta

Para uma lista com 1.000.000 de elementos:

- **Busca linear:** 1.000.000 verificações no pior caso
- **Busca binária:** 20 verificações no pior caso

## Por que "logarítmico"?

Porque usa logaritmos na base 2. Cada passo corta o problema pela metade:

- log₂(100) ≈ 7 (2⁷ = 128)
- log₂(1.000) ≈ 10 (2¹⁰ = 1.024)  
- log₂(1.000.000) ≈ 20 (2²⁰ = 1.048.576)

## Resumo

- **Linear:** Bom para listas pequenas ou quando não há ordem
- **Logarítmico:** Muito eficiente para listas grandes e ordenadas