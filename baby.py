def read_file(filename,sep):
  with open(filename,'r') as file:
    data = file.readlines()
    for d in data:
      print(d)
    sum = 10 + 30
    print("The addtion of 10 + 30 = ",sum)

read_file("sample-resource/testdata.txt",",")
