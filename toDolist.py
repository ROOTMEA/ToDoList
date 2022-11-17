print("""
1-ToDoList
2-Liste Oku
q-Çıkış
""")

while True:
    seç=input("Seç: ")
    
    if seç=="q":
        break
    elif seç == "1":
        listName=input("Liste Adı: ")
        toDoList=open(listName,"w")
        while True:
            icerik=input("Yapılacaklar: ")
            if icerik == "q":
                toDoList.close()
                break
            else:
                toDoList.write("{}\n".format(icerik))
    elif seç == "2":
        listebul=input("Okunacak Liste Adı: ")
        listOku=open(listebul,"r")
        print(listOku.read())
        listOku.close()
        