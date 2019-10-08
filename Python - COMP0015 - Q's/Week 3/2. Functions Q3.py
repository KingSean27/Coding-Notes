
def square_line(min_val, max_val):
  start_val = min_val
  line = ""
  line_number = 0
  for i in range(min_val, max_val + 1):
    for i in range(start_val, max_val + 1):
      line += str(i)
    for i in range(min_val, min_val + line_number):
      line += str(i)
    start_val += 1
    line_number += 1
    line += "\n"
  return line  

def main():
  min_val = int(input("Enter your minimum value: "))
  max_val = int(input("Enter your maximum value: "))
  
  if max_val <= min_val:
    quit()
  else:
    print(str(square_line(min_val, max_val)))
    
if __name__== "__main__":
  main()
