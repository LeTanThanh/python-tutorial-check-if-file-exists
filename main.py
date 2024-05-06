if __name__ == "__main__":
  # Using os.path.exists() function to check if a file exists

  import os.path

  print(os.path.exists("readme.txt"))

  from os.path import exists as file_exist

  print(file_exist("readme.txt"))

  # Using the pathlib module to check if a file exists

  from pathlib import Path

  path = Path("readme.txt")
  print(path.is_file())
