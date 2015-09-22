#putting each word in a array
string[0] = "Oxo";
string[1] = "OXO";
string[2] = "123454321";
string[3] = "ROTATOR";
string[4] = "12345 54321";

i=0;
while i<5:
  string[i] = string[i].casefold();
  rev_string = reversed(string[i]);

  if list(string[i] == rev_string):
    print("True")
  else
    print("False")

  i+=1

