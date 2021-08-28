import random
def main():
  print("Hello World")

  f=open("quotes.txt")
  quotes = f.readlines()
  f.close()
  print(quotes)
  
  # first line
  print(quotes[0])
  
  last =13
  rnd = random.randint(0,last)
  
  #rand line
  print(quotes[rnd])
  
  # last line
  print(quotes[len(quotes)-1])
 
if __name__== "__main__":
  main()
