w, h = map(int, input().split())
print("{:.2f}".format(round(w/(h/100)**2, 3)))
