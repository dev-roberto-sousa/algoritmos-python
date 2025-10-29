# Diferença entre Lista e Array

## Array (Vetor/Arranjo)

**Características principais:**
- Tamanho fixo: uma vez criado, não pode mudar de tamanho
- Todos os elementos são do mesmo tipo (inteiros, strings, etc.)
- Armazenamento contíguo na memória: os elementos ficam um ao lado do outro
- Acesso muito rápido aos elementos por índice

**Exemplo prático:** Uma prateleira com divisórias fixas - cada espaço tem tamanho igual e você não pode adicionar ou remover divisórias.

## Lista

**Características principais:**
- Tamanho dinâmico: pode crescer ou diminuir durante a execução
- Pode conter elementos de tipos diferentes
- Armazenamento não necessariamente contíguo na memória
- Flexível para adições e remoções

**Exemplo prático:** Uma fila de pessoas - pessoas podem entrar na fila (adição) ou sair da fila (remoção) a qualquer momento.

## Comparação direta

**Array:** Como uma caixa de ovos - tamanho fixo, cada espaço igual
**Lista:** Como um trem - vagões podem ser acoplados ou desacoplados

## Na programação

- **Arrays** são mais eficientes em memória e acesso, mas menos flexíveis
- **Listas** são mais flexíveis, mas podem ser menos eficientes em alguns casos

Em Python, o que chamamos de "lista" é na verdade uma implementação que combina características de ambos, oferecendo flexibilidade com bom desempenho.