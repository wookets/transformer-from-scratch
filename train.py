
with open("input.txt", "r", encoding="utf-8") as f: 
  text = f.read()

print("length of dataset in chars: ", len(text))

print(text[:1000])