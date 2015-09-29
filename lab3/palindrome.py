#definig string array
string = ["Oxo", "OXO", "123454321", "ROTATOR", "12345 54321", "RV"];

i=0;
#loop to test each string
while (i<len(string)):
  #put string to lowercse
  string[i] = string[i].lower()
  #reverse string and copy to rev_string
  rev_string = string[i][::-1]

  print "Is %s == %s ?" %(string[i], rev_string)
  #comparing string with reversed string
  if string[i] == rev_string:
    print("--->True<---")
  else:
    print("--->False<---")
  #increment i
  i+=1

