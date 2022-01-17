import json
with open("sample.json", "r", encoding = "utf-8") as f:
    data = json.load(f)



print(data)


for book in data:
    print(f"{'Titel:' : <10}{str(book['title']): >26} ")
    print(f"{'ISBN:' : <10}{str(book['isbn']): >26} ")
    print(f"{'Autoren:' : <10}{str(','.join(book['authors'])): >26} ")
    print()


lst1 = list(range(1,5))
lst2 = list(range(10,15))
dict = {'name': 'abc äöü', "list1": lst1, "list2": lst2}
print(json.dumps(dict, ensure_ascii=False, indent=4) )

