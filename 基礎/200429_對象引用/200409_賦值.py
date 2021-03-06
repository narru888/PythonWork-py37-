# 對不可變對象來說，變量保存的是真正對象還是共享對象之引用不太重要。
print("基本不可變類型，python做了優化，若值相等python會將他們指向同一個對象")
i1 = 10
i2 = 10
print(i1 is i2, id(i1), id(i2))
i1 = 5
print(i1 is i2, id(i1), id(i2))

print("可變類型則指向不同對象")
l1 = [1]
l2 = [1]
print(l1 is l2, id(l1), id(l2))

print("增量賦值")
i1 += i2
print(i1, id(i1))  # id改變
l1 += l2
print(l1, id(l1))  # id不變


"""
結論：
一、Python所有對象都有標識(ID)、類型和值，變量就像是便利貼(標註)般指向著對象。
二、在增量賦值方面，若為不可變對象，則會創造新的對象去接受新值；若為可變對象，則會就地修改。
"""
