# Explicação do Big O usando o exemplo dos quadrados

## O contexto do livro

O autor usa dois métodos diferentes para encontrar um quadrado específico em uma folha com 16 quadrados:

## Método 1: Verificar um por um (O(n))

Imagine que você tem uma folha com 16 quadrados numerados, mas desordenados. Para encontrar o quadrado número 8:

- Você olha para o primeiro quadrado: não é o 8
- Olha para o segundo: não é o 8  
- Olha para o terceiro: não é o 8
- ... e assim por diante até encontrar

No pior caso, você precisa verificar todos os 16 quadrados. Se tivesse 32 quadrados, no pior caso verificaria 32. Se tivesse 100, verificaria 100.

Isso é O(n) - o tempo cresce proporcionalmente ao número de elementos.

## Método 2: Dobrar o papel (O(log n))

Agora imagine que os quadrados estão ORDENADOS e organizados em uma grade 4x4. Para encontrar o quadrado número 8:

- Primeira dobra: você dobra o papel na metade e vê que o 8 está na metade inferior
- Segunda dobra: dobra a metade inferior ao meio e vê que o 8 está na metade esquerda  
- Terceira dobra: dobra essa seção ao meio e vê que o 8 está na metade superior
- Quarta dobra: dobra essa seção e encontra exatamente o quadrado 8

Com apenas 4 dobras (passos) você encontrou o quadrado entre 16 possibilidades.

## A relação com logaritmos

16 quadrados = 4 dobras porque 2^4 = 16, ou dito de outra forma: log₂(16) = 4

Se tivesse 32 quadrados: log₂(32) = 5 dobras
Se tivesse 64 quadrados: log₂(64) = 6 dobras

Veja que mesmo dobrando o número de quadrados (de 32 para 64), o número de dobras só aumenta de 5 para 6.

## Big O resume isso

- O(n): se dobrar os dados, dobra o tempo
- O(log n): se dobrar os dados, o tempo aumenta muito pouco

O exemplo das dobras mostra como um problema grande pode ser resolvido em poucos passos quando conseguimos eliminar metade das possibilidades a cada passo.