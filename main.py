def toBinary():
  num = int(input("Insira seu número: "))
  numBi = ''
  while num >= 1:
    numBi += str(num % 2)
    num = int(num / 2)

  numBi = numBi[::-1]
  print('Seu número em binário é: ' + numBi)


def toDecimal():
  i = 0
  num = str(input("Insira seu número: "))
  num = num[::-1]
  numDec = 0
  numArr = [char for char in num]
  while i < len(numArr):
    con = (int(numArr[i]) * (2**i))
    numDec += con
    i += 1
  print("Seu número em decimal é: ", numDec)


print("Que tipo de conversão você quer fazer?")
tipo = int(input("\n 1 - Decimal -> Binário \n 2 - Binário -> Decimal \n"))
if tipo == 1:
  toBinary()
elif tipo == 2:
  toDecimal()
