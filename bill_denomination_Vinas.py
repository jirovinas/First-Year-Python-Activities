money = eval(input("Enter an amount: "))
onethousand = money //1000
rem1 = money % 1000
fivehundred = rem1 //500
rem2 = rem1 % 500
twohundred = rem2 //200
rem3 = rem2 % 200
onehundred = rem3 //100
rem4 = rem3 % 100
fifty = rem4 //50
rem5 = rem4 % 50
twenty = rem5 //20
rem6 = rem5 % 20
ten = rem6 //10
rem7 = rem6 % 10
five = rem7 //5
rem8 = rem7 % 5
one = rem8 //1

print(str(onethousand )+ " - 1000")
print(str(fivehundred )+ " - 500")
print(str(twohundred )+ " - 200")
print(str(onehundred )+ " - 100")
print(str(fifty )+ " - 50")
print(str(twenty )+ " - 20")
print(str(ten )+ " - 10")
print(str(five )+ " - 5")
print(str(one )+ " - 1")
