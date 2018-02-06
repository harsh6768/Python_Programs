principle=10000
rate=6
time =5
i=(principle*rate*time)/100
print(principle)

#INTEREST
print(i)

for i in range(5):
    i = (principle * rate * time) / 100
    compound_interest=i+principle
    principle=compound_interest
    print(compound_interest)


