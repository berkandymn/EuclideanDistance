
#%%
points=[]
distances=[]
def euclideanDistance(x,y):
    euclid=0
    for k in range(len(x)):
        euclid+=(x[k]-y[k])*(x[k]-y[k])
    euclid **=(1/2)
    return euclid


#%%
while True:
    secenek = input("\n***MENU***\n1 - Nokta Gir \n2 - Öklid Hesapla \n3 - Mesafeleri Yazdır \n4 - Çıkış ")
    if secenek=="1":
        x1=int(input("X1"))
        y1=int(input("Y1"))
        x2=int(input("X2"))
        y2=int(input("Y2"))
        points.append(((x1,y1),(x2,y2)))
    elif secenek=="2":
        for sayi in points:
            sonuc=euclideanDistance(sayi[0],sayi[1])
            distances.append(sonuc)
    elif secenek=="3":
        print("Hesaplanan Öklid Uzaklık vektörleri \n")
        list(map(print,distances))
        #print(distances)
    elif secenek=="4":
        break
                

# %%
