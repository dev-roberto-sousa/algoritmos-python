**método sistemático** para analisar qualquer algoritmo.

## Análise da Função Fatorial

Para o algoritmo `factorial(n)`:

```python
def factorial(n):
    if n == 0:           # Operação constante: O(1)
        return 1         # Operação constante: O(1)
    else:
        return n * factorial(n - 1)  # Multiplicação O(1) + chamada recursiva
```

### Passo a Passo para Análise:

**1. Identificar o padrão de chamadas:**
- Cada chamada de `factorial(n)` faz **uma** chamada recursiva para `factorial(n-1)`
- Isso continua até `factorial(0)`

**2. Contar o número total de chamadas:**
- `factorial(n)` → `factorial(n-1)` → `factorial(n-2)` → ... → `factorial(0)`
- **Total: n + 1 chamadas** (de n até 0)

**3. Analisar o trabalho por chamada:**
- Cada chamada executa operações **constantes**: comparação, multiplicação, return
- **Custo por chamada: O(1)**

**4. Calcular complexidade total:**
```
T(n) = Número de chamadas × Custo por chamada
T(n) = (n + 1) × O(1) = O(n)
```

**Portanto, a complexidade é O(n)**

---

## Método Geral para Análise de Algoritmos

Aqui está seu **passo a passo** para analisar qualquer algoritmo:

### 📋 **Checklist para Análise**

**1. Identifique a operação fundamental:**
- O que o algoritmo mais executa? (comparações, atribuições, etc.)

**2. Conte quantas vezes ela é executada:**
- Em função do tamanho da entrada `n`

**3. Escreva a função de complexidade T(n):**
- Expresse matematicamente o número de operações

**4. Simplifique usando notação O():**
- Mantenha apenas o termo de maior crescimento
- Ignore constantes e termos de menor ordem

---

## 🎯 **Exemplos Práticos**

### **Exemplo 1: Busca Linear**
```python
def busca_linear(arr, alvo):
    for i in range(len(arr)):      # n iterações
        if arr[i] == alvo:         # O(1) por iteração
            return i
    return -1
```
**Análise:** O(n) - pior caso percorre todo o array

### **Exemplo 2: Loops Aninhados**
```python
def pares(n):
    for i in range(n):         # n iterações
        for j in range(n):     # n iterações por i
            print(i, j)        # O(1)
```
**Análise:** 
- Loop externo: n vezes
- Loop interno: n vezes por iteração externa
- **Total: n × n = O(n²)**

### **Exemplo 3: Algoritmo Recursivo Complexo**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```
**Análise:** 
- Cada chamada gera **2** chamadas recursivas
- Forma uma árvore binária de chamadas
- **Complexidade: O(2ⁿ)** (exponencial)

---

## 📊 **Guia Rápido de Complexidades Comuns**

| Padrão | Complexidade | Exemplo |
|--------|-------------|---------|
| **Operação única** | O(1) | Acesso a array por índice |
| **Loop simples** | O(n) | Busca linear |
| **Loops aninhados** | O(n²) | Comparar todos os pares |
| **Dividir e conquistar** | O(log n) | Busca binária |
| **Recursão simples** | O(n) | Fatorial |
| **Recursão dupla** | O(2ⁿ) | Fibonacci ingênuo |
| **Triplo loop** | O(n³) | Multiplicação de matrizes |

---

## 🔍 **Dica Prática**

**Pergunte-se: "Se eu dobrar o tamanho da entrada, o que acontece com o tempo?"**
- Se dobrar → O(n)
- Se quadruplicar → O(n²)  
- Se aumentar pouco → O(log n)
- Se explodir → O(2ⁿ)

Para o fatorial: dobrar `n` **dobra** o número de operações → **O(n)**

Quer praticar com algum algoritmo específico? Posso te guiar através da análise!