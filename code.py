def funargs(normall,*args,**kwargs):
    print(normall)
    for lst in args:
        print(lst)
    for key,value in kwargs.items():
        print(f"{key} eats {value}")    
lst=["asjad","ansar","ali","bilal"]
normall="asjad rizvi"
kw={"asjad":"bbq","ansar":"jo mil jaye"}
funargs(normall,*lst,**kw)
