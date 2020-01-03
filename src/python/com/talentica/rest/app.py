from flask import Flask, request
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

class TwoSidedPrimeNumber(Resource):
    def get(self, num):
        return self.isNumberTwoSidedPrime(num)


    def isNumberTwoSidedPrime(self, num):
        if num <= 3 :
            return num > 1
        elif (num % 2) == 0 or (num % 3) == 0:
            return False
        isPrime = self.isNumberPrime(num)
        if isPrime:
            isPrimeFromRight = self.isPrimeFromRight(num)
            if isPrimeFromRight:
                isPrimeFromLeft = self.isPrimeFromLeft(num)
                if isPrimeFromLeft:
                    return True
        return False
    def isNumberPrime(self, num):
        count = 5
        while count * count <= num:
            if num % count == 0 or num % (count + 2) == 0:
                return False
            count = count + 6
        return True
    def isPrimeFromRight(self, num):
        newNum = num // 10
        while newNum > 0:
            if not self.isNumberPrime(newNum):
                return False
            newNum = newNum // 10
        return True

    def isPrimeFromLeft(self, num):
        countOfDigitsInNum = (math.log10(num) + 1)
        newNum = num % countOfDigitsInNum
        while newNum > 0:
            if not self.isNumberPrime(newNum):
                return False
            newNum = newNum % countOfDigitsInNum
        return True

api.add_resource(TwoSidedPrimeNumber, '/<int:num>')
app.run()