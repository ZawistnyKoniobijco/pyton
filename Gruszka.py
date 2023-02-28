

a="gruszek"
b="gruszka"
c="gruszki"

d= ['gruszek', 'gruszka', 'gruszki','gruszki']
# print(d)


sample_set = set(['gruszek','gruszka','gruszki','gruszki'])

# print(sample_set)


def liczygruszkator(grucha):
    
    if grucha == 1:
        return "gruszka"
    if grucha >=2 and grucha <=4:
        return "gruszki"
    if grucha == 0 or grucha == 5:
        return "gruszek"

for i in range(0,6):   

    print(i,liczygruszkator(i))

n1 = range(0)

n2 = range(1)

n3 = range(2,5)

# s1 = random.choice(['a','b','c'])
# print(s1)



