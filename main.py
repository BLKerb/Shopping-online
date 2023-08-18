#==============Meni prensipal====================
import products
print("=======================Byenvini kay BLK-boutik !=======================")
print("\n=======================Meni prensipal=======================")
		
print("\nChwazi ak yon chif sa ou vle fè a !")
print("1- Verifye pwodwi ki disponib yo")
print("2- verifye panye")
print("3- femen")
Chwa = int(input("\nChwazi yon opsyon : "))
if Chwa == 1:
    products.pwodwi()
elif Chwa == 2:
    print("OU POKO ACHTE ANYEN, PA GEN ANYEN NAN PANYE!!!!\n")
    menu={"pizza": 3.00,
      "nachos": 4.50,
      "popcorn": 6.00,
      "fries": 2.50,
      "chips": 2.50,
      "pretzel": 3.50,
      "soda": 3.00,
      "lemonade": 4.25}
    chwa=int(input("\nPeze nenpot touch pouw kite,\nPeze 1 siw vle achte :"))
    if chwa == 1:
        products.pwodwi()
    else:
        print("Babay")
else:
    print("mesi, orevwa!!!")				

