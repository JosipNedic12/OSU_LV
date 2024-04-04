try:
    broj = float(input('Unesite broj:'))
except:
    print("Molim unesite broj!a")
if broj>1 or broj<0:
    print("Unešeni broj nije u rasponu od 0 do 1!")
elif broj >= 0.9 and broj <=1:
    print("Kategorija: A")
elif broj<0.9 and broj >=0.8:
    print("Kategorija: B")
elif broj<0.8 and broj >=0.7:
    print("Kategorija: C")
elif broj<0.7 and broj >=0.6:
    print("Kategorija: D")
elif broj<0.6:
    print("Kategorija: F")
