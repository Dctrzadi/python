#write a program to greet all the person names stores in a list 'l' and which starts which S
l=["Somi","Shivam","Sonu","Riya","Shubhi","Lucky"]
for name in l:
    if name.startswith("S"):
        print(f"hello{name}")
        