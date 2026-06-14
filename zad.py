cos = input("podaj text ")
if len(cos) > 10:
    print("wynik: ", cos[:10] + "...")
else:
    print("wynik: ", cos)