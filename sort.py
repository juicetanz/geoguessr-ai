import os
import shutil

trainPath = 'data/train/'
testPath = 'data/test/'
valPath = 'data/val/'

# Move 20% of data to val
for country in os.listdir(trainPath):
  # Add country folders
  os.makedirs(valPath + country, exist_ok = True)
  for idx, img in enumerate(os.listdir(trainPath + country)):
    if idx % 5 == 0:
      print(trainPath + country + '/' + img, "TO", valPath + country + '/' + img)
      if len(os.listdir(trainPath + country)) <= 3:
        shutil.copy(trainPath + country + '/' + img, valPath + country + '/' + img)
      else:
        shutil.move(trainPath + country + '/' + img, valPath + country + '/' + img)

# Move half of val data to test
for country in os.listdir(valPath):
  os.makedirs(testPath + country, exist_ok = True)
  for idx, img in enumerate(os.listdir(valPath + country)):
    if idx % 2 == 0:
      print(valPath + country + '/' + img, "TO", testPath + country + '/' + img)
      # Copy the file instead of moving if there are few files
      if len(os.listdir(trainPath + country)) <= 3:
        shutil.copy(valPath + country + '/' + img, testPath + country + '/' + img)
      else:
        shutil.move(valPath + country + '/' + img, testPath + country + '/' + img)
