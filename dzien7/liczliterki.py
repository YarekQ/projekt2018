import os
from trypolicz import policz
zdanie="Ala ma kota"
znak="Al"
#poprawiamy:
try:
    zdanie=policz(zdanie,znak)
except ValueError:
    znak=znak[1]
    znalezione=policz(zdanie,znak)

print(f"W zdaniu jest {znalezione} podstringów")
os.getcwd()
info=os.path.splitext(r"scieżka")