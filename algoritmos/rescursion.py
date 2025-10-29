def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)    
    
countdown(10)

# 5! = 5 . 4 . 3 . 2 . 1 = 120

n = 5
fact = 1

"""
O (1, n + 1) na função range() cria uma sequência de números inteiros para o loop.
O 1 é o número de início da sequência (inclusive).
O n + 1 é o número de parada da sequência (exclusivo). 
Isso significa que a sequência de números irá começar em 1 e terminará em n.
O n + 1 é o limite superior e não é incluído. Por exemplo, se o valor de n for 5,
a função range(1, 5 + 1) se torna range(1, 6),
e a sequência gerada será 1, 2, 3, 4, 5. O loop irá executar cinco vezes, 
com a variável i assumindo cada um desses valores em cada iteração.
"""
for i in range(1, n + 1): 
    print(i)
    fact = fact * i

print("The factorial of 5 is : ", end="")
print(fact)
    
def factorial(n):
    if n == 0: # Caso base
        return 1
    else: # Caso recursivo
        return n * factorial(n - 1)
    
print(factorial(10))