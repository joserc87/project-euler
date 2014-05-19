#!/usr/bin/python


def sumDigitos (num, exp):
    sum=0L
    while num>0:
        sum += (num%10)**exp
        num/=10
    return sum
        
# Con un número de d dígitos, el máximo sería d*9^5=d*59049, pero el
# número sería 10^d: 10^d= d*9^5 <->10^(d-1)=9^5->d-1 =
# log10(9^5)->d=log10(9^5)+1=5.77->hasta 6 dígitos. -> comprobar 10
# millones de elementos

sumTotal = 0L
nums = range (2, 999999)
for i in nums:
    if i == sumDigitos (i, 5):
        sumTotal += i;
print sumTotal
