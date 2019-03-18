divisors = [1000, 100, 10, 1]
algarisms = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def decimal():
	print("\n\n")
	print("##################################################")
	print("### CONVERSÃO DE NÚMEROS DECIMAIS PARA ROMANOS ###")
	print("##################################################")
	print("\nDigite o número decimal a ser convertido:")
	decimalNumber = int(input("> "))

	# There are only positive numbers in the roman numbers
	if decimalNumber <= 0:
		print("\nNúmero inexistente no sistema de algarismos romanos\n")
	else:
		romanNumber = convert2roman(decimalNumber, 0, "")
		print("\nDecimal - Romano")
		print(str(decimalNumber) + " - " + romanNumber + "\n")

def convert2roman(number, i, romanNumber):
	""" Convert a decimal number into a roman number
	The conversion is basically done by segregating the number into a thousands, hundreds, tens and units parts.
	Then conver each part in that sequence.

	Arguments:
	number -- decimal number to be converted
	i -- the index of the current divisor
	romanNumber -- result string of the conversion

	"""

	divisor = divisors[i]
	quotient = number // divisor
	remain = number % divisor

	if remain == 0:
		if quotient > 0:
			# When the roman number could have algarisms in a row (3 at maximum).
			if quotient < 4:
				letter = algarisms[divisor]
				romanNumber = convert2roman(number-divisor, i, romanNumber + letter)
				
				return romanNumber
			# Special case when the subtraction is needed to represent the number.
			# When a lower value algarism is immediately left to a greater algarism value
			elif quotient == 4 or quotient == 9:
				letter = algarisms[divisor]
				letter = letter + algarisms[number+divisor]
				romanNumber = convert2roman(remain, i-1, romanNumber + letter)
				
				return romanNumber
			# Need to add the algarism that is divisible by 5 (V, L, D)
			else:
				letter = algarisms[divisor*5]
				romanNumber = convert2roman(number - divisor*5, i, romanNumber + letter)
				
				return romanNumber
		else:
			return romanNumber
	else:
		if remain == number:
			romanNumber = convert2roman(number, i+1, romanNumber)
			
			return romanNumber
		else:
			# When the roman number could have algarisms in a row (3 at maximum).
			if quotient < 4:
				letter = algarisms[divisor]
				romanNumber = convert2roman(number-divisor, i, romanNumber + letter)
				
				return romanNumber
			# Special case when the subtraction is needed to represent the number.
			# When a lower value algarism is immediately left to a greater algarism value
			elif quotient == 4 or quotient == 9:
				letter = algarisms[divisor]
				letter = letter + algarisms[quotient*divisor + divisor]
				romanNumber = convert2roman(remain, i-1, romanNumber + letter)
				
				return romanNumber
			# Need to add the algarism that is divisible by 5 (V, L, D)
			else:
				letter = algarisms[divisor*5]
				romanNumber = convert2roman(number - divisor*5, i, romanNumber + letter)
				
				return romanNumber

def roman():
	print("\n\n")
	print("##################################################")
	print("### CONVERSÃO DE NÚMEROS ROMANOS PARA DECIMAIS ###")
	print("##################################################")
	print("\nDigite o número romano a ser convertido:")
	rom = input("> ")

	# Assure that de input is in upper case
	romanNumber = rom.upper()
	decimalNumber = convert2decimal(romanNumber)

	if decimalNumber < 0:
		print("\nNúmero inexistente no sistema romano\n")
	else:
		print("\nRomano - Decimal")
		print(romanNumber + " - " + str(decimalNumber) + "\n")

def convert2decimal(number):
	""" Convert a roman number into a decimal number
	The conversion is done by adding the roman algarism value.
	But if the value of the next algarism is greater than the current,
	Then a subtraction is done instead.

	Arguments:
	number -- roman number to be converted

	"""

	first = True
	isRoman = True
	subtractionUsed = False
	decimal = 0
	last = 0
	cont = 0

	for algarism in number:
		try:
			currentValue = values[algarism]
		except: # Check if there is a non roman algarism
			isRoman = False
			break

		if first:
			decimal += currentValue
			last = currentValue
			first = False
			cont += 1
		else:
			# Check the presence of repeated algarisms
			if currentValue == last:
				cont += 1
				firstLetter = str(currentValue)[0]
				if cont > 3 or firstLetter == '5' or subtractionUsed:
					isRoman = False
					break

				subtractionUsed = False
				decimal += currentValue
				last = currentValue
			else:
				cont = 1
				# Just add if the value of the current algarism is lower than the before algarism
				if currentValue < last:
					subtractionUsed = False
					decimal += currentValue
					last = currentValue
				# Otherwise subtract
				else:
					if not subtractionUsed:
						firstLetter = str(last)[0]
						if firstLetter == '1':
							if currentValue == 5*last or currentValue == 10*last:
								decimal -= last
								decimal += currentValue-last
								subtractionUsed = True
							else:
								isRoman = False
								break	
						else:
							isRoman = False
							break
					else:
						isRoman = False
						break

	if isRoman:
		return decimal
	else:
		return -1

if __name__ == '__main__':
	logic = True

	# Menu
	while logic:
		print("\n(Conversão válida somente para números de 1 a 3999)")
		print("\nDigite:")
		print("0 - Encerrar")
		print("1 - Converter um número decimal em romano")
		print("2 - Converter um número romano em decimal")

		try:
			op = int(input("> "))
			
			if op == 0:
				logic = False
			elif op == 1:
				decimal()
			elif op == 2:
				roman()
			else:
				print("\nOpção Inválida!\n")
		except KeyboardInterrupt:
			break
		except: 
			print("\nOpção Inválida!\n")

	print("\n\nEncerrando aplicação...")