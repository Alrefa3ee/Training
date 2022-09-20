text = "adad"

length = int(len(text) / 2)
if text[:length] == text[length:]:
    print("Double String")
else:
    print("Not Double String")
