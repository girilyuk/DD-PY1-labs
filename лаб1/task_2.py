# TODO Найдите количество книг, которое можно разместить на дискете

Simvol = 4
Simvol_in_strok = 25
Strok = 50
Str = 100
Books = ((1024*1024*1.44)/(Simvol*Simvol_in_strok*Strok*Str))
print("Количество книг, помещающихся на дискету:", round(Books))