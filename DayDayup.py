dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
        print('{:.2f}'.format(dayup))
    else:
        dayup = dayup*(1+dayfactor)
        print('{:.2f}'.format(dayup))
print('{:.2f}'.format(dayup))