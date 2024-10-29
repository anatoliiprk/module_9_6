print('------\nЗадание по теме "Генераторы"\n------')

def all_variants(text):
    for i in range(len(text)):
        i += 1
        for j in range(len(text)):
            yield text[j:i]
            i += 1
            if i > len(text):
                break

a = all_variants('abcd')
for i in a:
    print(i)

print('------')