numero = int(input("Digite um número inteiro: "))


def sequencia_fibonacci(n):
  fib_sequencia = [0, 1]
  while fib_sequencia[-1] < n:
    fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
  return fib_sequencia

def e_fibonacci(num):
   fib_sequencia = sequencia_fibonacci(num)
   if num in fib_sequencia:
      return True
   else:
      return False

if e_fibonacci(numero):
  print(f"O número {numero} pertence á sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence a sequência de Fibonacci.")
