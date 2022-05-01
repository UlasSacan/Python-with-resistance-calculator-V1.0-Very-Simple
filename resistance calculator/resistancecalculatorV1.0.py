"Project Owner:       Ulas Sacan"
"Project Name:        (Very simple)resistance calculator V1.0"
"About: The project has been created with if else for now, and calculations with 4 and 5 bands can be made. V1.0"

print("**********DİRENC HESAPLAMA PROGRAMI**********\n")


req = int(input("kaç bantli direnc hesaplamak istersiniz: "))


if req == 4:
    renkbir = str(input("ilk rengi giriniz: "))
    renkiki = str(input("ikinci rengi giriniz: "))
    renkuc = str(input("ucuncu rengi giriniz: "))
    renktolerans = str(input("tolerans rengi giriniz: "))

    if renkbir == "siyah":
        renkbir = 0
    if renkbir == "kahverengi":
        renkbir = 1
    if renkbir == "kirmizi":
        renkbir = 2
    if renkbir == "turuncu":
        renkbir = 3
    if renkbir == "sari":
        renkbir = 4
    if renkbir == "yesil":
        renkbir = 5
    if renkbir == "mavi":
        renkbir = 6
    if renkbir == "mor":
        renkbir = 7
    if renkbir == "gri":
        renkbir = 8
    if renkbir == "beyaz":
        renkbir = 9

    if renkiki == "siyah":
        renkiki = 0
    if renkiki == "kahverengi":
        renkiki = 1
    if renkiki == "kirmizi":
        renkiki = 2
    if renkiki == "turuncu":
        renkiki = 3
    if renkiki == "sari":
        renkiki = 4
    if renkiki == "yesil":
        renkiki = 5
    if renkiki == "mavi":
        renkiki = 6
    if renkiki == "mor":
        renkiki = 7
    if renkiki == "gri":
        renkiki = 8
    if renkiki == "beyaz":
        renkiki = 9

    if renkuc == "siyah":
        renkuc = 0
    if renkuc == "kahverengi":
        renkuc = 1
    if renkuc == "kirmizi":
        renkuc = 2
    if renkuc == "turuncu":
        renkuc = 3
    if renkuc == "sari":
        renkuc = 4
    if renkuc == "yesil":
        renkuc = 5
    if renkuc == "mavi":
        renkuc = 6
    if renkuc == "mor":
        renkuc = 7
    if renkuc == "gri":
        renkuc = 8
    if renkuc == "beyaz":
        renkuc = 9

    if renktolerans == "siyah":
        renktolerans = 0
    if renktolerans == "kahverengi":
        renktolerans = 1
    if renktolerans == "kirmizi":
        renktolerans = 2
    if renktolerans == "turuncu":
        renktolerans = 3
    if renktolerans == "sari":
        renktolerans = 4
    if renktolerans == "yesil":
        renktolerans = 5
    if renktolerans == "mavi":
        renktolerans = 6
    if renktolerans == "mor":
        renktolerans = 7
    if renktolerans == "gri":
        renktolerans = 8
    if renktolerans == "beyaz":
        renktolerans = 9
    if renktolerans == "altin":
        renktolerans = 5
    if renktolerans == "gumus":
        renktolerans = 10

    sonuc = f"Direnc Degeri: {renkbir}{renkiki*10**renkuc}(Ω)ohm Tolerans Degeri: % {renktolerans}"
    print(sonuc)

if req == 5:
    renkbir = str(input("ilk rengi giriniz: "))
    renkiki = str(input("ikinci rengi giriniz: "))
    renkuc = str(input("ucuncu rengi giriniz: "))
    renkdort = str(input("dorduncu rengi giriniz: "))
    renktolerans = str(input("tolerans rengi giriniz: "))    
    if renkbir == "siyah":
        renkbir = 0
    if renkbir == "kahverengi":
        renkbir = 1
    if renkbir == "kirmizi":
        renkbir = 2
    if renkbir == "turuncu":
        renkbir = 3
    if renkbir == "sari":
        renkbir = 4
    if renkbir == "yesil":
        renkbir = 5
    if renkbir == "mavi":
        renkbir = 6
    if renkbir == "mor":
        renkbir = 7
    if renkbir == "gri":
        renkbir = 8
    if renkbir == "beyaz":
        renkbir = 9

    if renkiki == "siyah":
        renkiki = 0
    if renkiki == "kahverengi":
        renkiki = 1
    if renkiki == "kirmizi":
        renkiki = 2
    if renkiki == "turuncu":
        renkiki = 3
    if renkiki == "sari":
        renkiki = 4
    if renkiki == "yesil":
        renkiki = 5
    if renkiki == "mavi":
        renkiki = 6
    if renkiki == "mor":
        renkiki = 7
    if renkiki == "gri":
        renkiki = 8
    if renkiki == "beyaz":
        renkiki = 9

    if renkuc == "siyah":
        renkuc = 0
    if renkuc == "kahverengi":
        renkuc = 1
    if renkuc == "kirmizi":
        renkuc = 2
    if renkuc == "turuncu":
        renkuc = 3
    if renkuc == "sari":
        renkuc = 4
    if renkuc == "yesil":
        renkuc = 5
    if renkuc == "mavi":
        renkuc = 6
    if renkuc == "mor":
        renkuc = 7
    if renkuc == "gri":
        renkuc = 8
    if renkuc == "beyaz":
        renkuc = 9

    if renkdort == "siyah":
        renkdort = 0
    if renkdort == "kahverengi":
        renkdort = 1
    if renkdort == "kirmizi":
        renkdort = 2
    if renkdort == "turuncu":
        renkdort = 3
    if renkdort == "sari":
        renkdort = 4
    if renkdort == "yesil":
        renkdort = 5
    if renkdort == "mavi":
        renkdort = 6
    if renkdort == "mor":
        renkdort = 7
    if renkdort == "gri":
        renkdort = 8
    if renkdort == "beyaz":
        renkdort = 9

    if renktolerans == "siyah":
        renktolerans = 0
    if renktolerans == "kahverengi":
        renktolerans = 1
    if renktolerans == "kirmizi":
        renktolerans = 2
    if renktolerans == "turuncu":
        renktolerans = 3
    if renktolerans == "sari":
        renktolerans = 4
    if renktolerans == "yesil":
        renktolerans = 5
    if renktolerans == "mavi":
        renktolerans = 6
    if renktolerans == "mor":
        renktolerans = 7
    if renktolerans == "gri":
        renktolerans = 8
    if renktolerans == "beyaz":
        renktolerans = 9
    if renktolerans == "altin":
        renktolerans = 5
    if renktolerans == "gumus":
        renktolerans = 10
        
    sonuc = f"Direnc Degeri: {renkbir}{renkiki}{renkuc*10**renkdort}(Ω)ohm Tolerans Degeri: %{renktolerans}"
    print(sonuc)

    

# if req == 6:
#     renkbir = str(input("ilk rengi giriniz: "))
#     renkiki = str(input("ikinci rengi giriniz: "))
#     renkuc = str(input("ucuncu rengi giriniz: "))
#     renkdort = str(input("dorduncu rengi giriniz: "))
#     renkbes = str(input("dorduncu rengi giriniz: "))
#     renktolerans = str(input("tolerans rengi giriniz: "))    
#     if renkbir == "siyah":
#         renkbir = 0
#     if renkbir == "kahverengi":
#         renkbir = 1
#     if renkbir == "kirmizi":
#         renkbir = 2
#     if renkbir == "turuncu":
#         renkbir = 3
#     if renkbir == "sari":
#         renkbir = 4
#     if renkbir == "yesil":
#         renkbir = 5
#     if renkbir == "mavi":
#         renkbir = 6
#     if renkbir == "mor":
#         renkbir = 7
#     if renkbir == "gri":
#         renkbir = 8
#     if renkbir == "beyaz":
#         renkbir = 9

#     if renkiki == "siyah":
#         renkiki = 0
#     if renkiki == "kahverengi":
#         renkiki = 1
#     if renkiki == "kirmizi":
#         renkiki = 2
#     if renkiki == "turuncu":
#         renkiki = 3
#     if renkiki == "sari":
#         renkiki = 4
#     if renkiki == "yesil":
#         renkiki = 5
#     if renkiki == "mavi":
#         renkiki = 6
#     if renkiki == "mor":
#         renkiki = 7
#     if renkiki == "gri":
#         renkiki = 8
#     if renkiki == "beyaz":
#         renkiki = 9

#     if renkuc == "siyah":
#         renkuc = 0
#     if renkuc == "kahverengi":
#         renkuc = 1
#     if renkuc == "kirmizi":
#         renkuc = 2
#     if renkuc == "turuncu":
#         renkuc = 3
#     if renkuc == "sari":
#         renkuc = 4
#     if renkuc == "yesil":
#         renkuc = 5
#     if renkuc == "mavi":
#         renkuc = 6
#     if renkuc == "mor":
#         renkuc = 7
#     if renkuc == "gri":
#         renkuc = 8
#     if renkuc == "beyaz":
#         renkuc = 9

#     if renkdort == "siyah":
#         renkdort = 0
#     if renkdort == "kahverengi":
#         renkdort = 1
#     if renkdort == "kirmizi":
#         renkdort = 2
#     if renkdort == "turuncu":
#         renkdort = 3
#     if renkdort == "sari":
#         renkdort = 4
#     if renkdort == "yesil":
#         renkdort = 5
#     if renkdort == "mavi":
#         renkdort = 6
#     if renkdort == "mor":
#         renkdort = 7
#     if renkdort == "gri":
#         renkdort = 8
#     if renkdort == "beyaz":
#         renkdort = 9

#     if renktolerans == "siyah":
#         renktolerans = 0
#     if renktolerans == "kahverengi":
#         renktolerans = 1
#     if renktolerans == "kirmizi":
#         renktolerans = 2
#     if renktolerans == "turuncu":
#         renktolerans = 3
#     if renktolerans == "sari":
#         renktolerans = 4
#     if renktolerans == "yesil":
#         renktolerans = 5
#     if renktolerans == "mavi":
#         renktolerans = 6
#     if renktolerans == "mor":
#         renktolerans = 7
#     if renktolerans == "gri":
#         renktolerans = 8
#     if renktolerans == "beyaz":
#         renktolerans = 9
#     sonuc = f"{renkbir},{renkiki}{renkuc}{renkdort*10**renktolerans}"
#     print(sonuc,"(Ω)ohm")