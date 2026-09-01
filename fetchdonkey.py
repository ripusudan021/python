with open("donkey.txt") as don:
    content = don.read()
    words = content.split()
    
    for i in range(len(words)):
        if words[i].lower() == "donkey":
            words[i] = "$$$$"
    print(words)

    updated_content= " ".join(words)
    with open("donkey.txt","w") as don:
        don.write(updated_content)
    print("file updated successfully!")


    # content = don.read()
    # l = content.split(" ")
    # print(l)
    # for i in range(len(l)):
    #     if l[i] == "donkey" or l[i] == "Donkey":
    #         l[i] = "####"
        
    # print(l)