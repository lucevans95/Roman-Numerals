values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
x = 0
while x !=1: 
  num = input(print("Input a number from 1-3999 to see it's representation in roman numerals"))
  num = int(num)
  copy = num
  if num > 3999:
    print("Number cannot exceed 3999")
  elif num < 0:
    print("Please enter a postive number")
  else:
    x = 1

roman = ""

while num > 0:
  index = 0
  for i in values:
    if num >= i:
      roman+=symbols[index]
      num-=i
      break 
    index+=1

print(str(copy) + " in roman numerals = " + roman)