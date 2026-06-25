from collections import Counter

dic = {
    'Codingal' : 2,
    'is' : 4,
    'best' : 2,
    'for' : 2,
    'coding' : 3
  
}

counts = Counter(dic.values())

print('Frequence of 2 is', counts[2], 'times')

