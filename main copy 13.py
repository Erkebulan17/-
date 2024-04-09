d=2
h=5
t=1

for r in range (d,h + 1):
    t *=r
    print(f"Сандардын көбейтіндісі {d} + {h} қоса алғанда :{t}")


J = int(input("J:"))    
p = sum (1 / e for e in range (1, J + 1 ) )
print(f"")
print("Қатардын суммасы  1 + 1/2 + 1/3 + … + 1/N тең:", p(J))