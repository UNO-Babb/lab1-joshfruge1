#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
  name = input("Give me a name: ")
  theme = input("Give me a theme: ")
  place = input("Give me a place: ")
  dotw = input("Give me a day of the week: ")
  time = input("Give me a time of day: ")
  verb = input("Give me a verb: ")
  animal = input("Give me an animal: ")
  body = input("Give me a body part: ")
  contact = input("Give me contact infomration: ")

  print(name, "is having a",theme,"party! It's going to be at",place,"on",dotw,". Please show up at",time,", or else you will be required to",verb,"a/an",animal,"with your",body,". RSVP at",contact, ".")
  #Print the story with the user supplied words

  #Cant sync changes???

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
