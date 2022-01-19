import random

user_input = input("Hi there, whats up? Want to stop chatting? Just type \"stop\": ")
good_input = ["good","great","yes","ok","well","fine","dandy","quite well"]
bad_input = ["bad","not good","no","awful"]

responses = ["Alright.","Okay.","Nice.","Cool." ]

def good_or_bad(answer,good,bad):
  if answer in good_input:
    print(good)
  elif answer in bad_input:
    print(bad)
  else:
    print("I'm not sure what to say to that")

if user_input != "stop":
  good_or_bad(user_input,"I'm glad to hear that!","Thats a shame.")

if user_input != "stop":
  if int(user_input) == 0:
    user_input = input("What's it like being an only child? ")
    good_or_bad(user_input,"I'm glad to hear that!","I'm sorry to hear that.")
  elif int(user_input) == 1:
    user_input = input("Cool! Do you have a brother or a sister? ")
    print(random.choice(responses))
  else:
    print(random.choice(responses))

if user_input != "stop":
  user_input = input("What's a hobby of yours? ")
if user_input != "stop":
  user_input = input("That's pretty cool! Tell me more!\nType something: ")
if user_input != "stop":
  user_input = input("How long have you had that hobby? ")
if user_input != "stop":
  print(random.choice(responses))

if user_input != "stop":
  user_input = input("Do you go to school? ")
if user_input != "stop":
  if user_input == "yes":
    user_input = input("Do you enjoy it? ")
    good_or_bad(user_input,"I'm glad to hear that!","I definitely hear ya. School sucks sometimes.")
  else:
    user_input("Ok, so what do you do for a living? ")
    user_input("Is this something you enjoy")
    good_or_bad(user_input,"I'm glad to hear that!","I'm sorry to hear that.")
if user_input != "stop":
  user_input = input("Just tell me more about yourself in general. Type \"stop\" if you don't want to talk anymore: ")
while user_input != "stop":
  print(random.choice(responses))
  user_input = ("Type something: ")