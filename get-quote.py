def main():
  print("Hello World")

  f=open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print(quotes)
  
  print(quotes[0])

if __name__== "__main__":
  main()
