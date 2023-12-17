import os

def handler(context):
  print("main")
  print(os.environ["TEST-VAR"])
