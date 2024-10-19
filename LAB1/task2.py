# TODO Найдите количество книг, которое можно разместить на дискете
symbcount=25
symb=4
strcount=50
pagecount=100
disc=1.44*1024*1024
otv=round(disc/(symbcount*symb*strcount*pagecount))
print("Количество книг, помещающихся на дискету:", otv)
