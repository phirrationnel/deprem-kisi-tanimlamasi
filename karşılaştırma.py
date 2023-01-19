karşılaştır = []

d1 = open("okuldaolanlar.txt", "r")
file_content1 = d1.read()

d2 = open("okuluniçindeolanlar.txt", "r")
file_content2 = d2.read()

içeridekalanlar = list( set(file_content1) - set(file_content2) )

karşılaştır.append(içeridekalanlar)

with open('karşılaştırma.txt', 'w') as fp:
    for item in karşılaştır:
        fp.write("%s\n" % item)





