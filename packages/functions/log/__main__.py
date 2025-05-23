import os

def main(args,context):
  msg = args.get("msg")
  #with open("logs.txt","r") as f:
  #  lines= f.readlines()

  lines= os.listdir()
        
  print(lines)
  print(os.getcwd())
  return {"body": lines}
