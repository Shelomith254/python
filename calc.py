class Calculator:
    def _init_(self, addition, subtraction, division, multiplication):
        self.addition = addition
        self.subtraction = subtraction
        self.division = division
        self.multiplication = multiplication

    def addition(self, *numbers):
        number= input('Enter numbers:')
        try:
            if numbers== 0:
                print('0')
            else:
                sum = 0
                for number in numbers[1:]:
                	sum+=number
                print(sum)
        except:
             print('ValueError')

    def multiplication(self, *numbers):
        numbers = input('Enter numbers:')
        try:
            if numbers == 0:
                print('0')
            else:
                product = 1
                for number in numbers:
                    product *= number
                print(product)
        except:
            print('ValueError')

    def division(self, dividend, divisor):
        dividend = input('Enter dividend:')
        divisor = input('Enter divisor:')
        try:
            if divisor == 0:
                print('0')
            else:
                answer = dividend / divisor
                print(answer)
        except:
            print('ValueError')

    def subtraction(self, *numbers):
        numbers = input('Enter numbers')
        try:
            if numbers == 0:
                print('0')
            else:
                difference = numbers[0]
                for number in numbers[1:]:
                    difference -= number
                print(difference)
        except:
            print('ValueError')