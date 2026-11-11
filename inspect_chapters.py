with open("index.html", encoding="utf-8") as f:
    text = f.read()

idx = text.find("lessonId.startsWith(\"c2_\")")
print(text[idx:idx+1500])
