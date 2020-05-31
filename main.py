from random import randint

shortest = 7 
longest = 10 
min_ascii = 33 
max_ascii = 126 

def randomPassword():
  randomLength = randint(shortest, longest)
  result = ""
  for i in range(randomLength):
    randomChar = chr(randint(min_ascii,max_ascii))
    result = result + randomChar

  return result
def main():
  print(f"Your random password is: {randomPassword()}")
if __name__ == "__main__":
  main()
