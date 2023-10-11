import random

first_names = [
    "John", "Alice", "Michael", "Emily", "David", "Sarah", "Daniel", "Olivia",
    "William", "Sophia", "Matthew", "Emma", "Christopher", "Ava", "James",
    "Lily", "Joseph", "Mia", "Robert", "Grace"
]

last_names = [
    "Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Anderson",
    "Martinez", "Jones", "Taylor", "Clark", "Lee", "Walker", "Hall", "Garcia",
    "Harris", "Robinson", "White", "Thomas", "Lewis"
]

crimes_sentences = [
    5,  # Arson
    2,  # Theft
    10,  # Armed Assault
    3,  # Burglary
    7,  # Robbery
    25,  # Homicide
    4,  # Fraud
    15,  # Drug Trafficking
    20,  # Kidnapping
    10,  # Carjacking
    8,  # Cybercrime
    2,  # Vandalism
    5,  # Forgery
    7,  # Embezzlement
    1,  # Shoplifting
    5,  # Identity Theft
    15,  # Money Laundering
    2,  # Stalking
    10,  # Sexual Assault
    10,  # Domestic Violence
    10  # Tax Fraud
]


def calculator(first_names, last_names, crimes_sentences):
  crimes = [
      "Arson", "Theft", "Armed Assault", "Burglary", "Robbery", "Homicide",
      "Fraud", "Drug Trafficking", "Kidnapping", "Carjacking", "Cybercrime",
      "Vandalism", "Forgery", "Embezzlement", "Shoplifting", "Identity Theft",
      "Money Laundering", "Stalking", "Sexual Assault", "Domestic Violence",
      "Tax Fraud"
  ]

  crimes_comitted = random.randint(0, len(crimes) - 1)
  first_name = random.randint(0, len(first_names) - 1)
  last_name = random.randint(0, len(last_names) - 1)

  print(
      f'the defendant, {first_names[first_name]} {last_names[last_name]} has been found guilty of: '
  )
  actual_sentence = 0
  for i in range(crimes_comitted):
    which_crime = random.randint(0, len(crimes) - 1)
    counts = random.randint(1, 25)
    print(f'{counts} counts of {crimes[which_crime]},')
    actual_sentence += crimes_sentences[which_crime] * counts
    crimes.pop(which_crime)
  while True:
    user_guess = input(
        f'how many years should {first_names[first_name]} {last_names[last_name]} be convicted?\n'
    )
    try:
      user_guess = int(user_guess)
      break
    except:
      print('please enter a number')
  if user_guess == actual_sentence:
    print('wowzas you got it!!!')
  elif user_guess in range(actual_sentence - 25, actual_sentence + 25):
    print(f'you got it within 25 years!!! it was {actual_sentence}')
  elif user_guess in range(actual_sentence - 50, actual_sentence + 50):
    print(f'you got it within 50 years!!! it was {actual_sentence}')
  elif user_guess in range(actual_sentence - 100, actual_sentence + 100):
    print(
        f'you got it within 100 years so uh pretty dog water, it was {actual_sentence}'
    )
  else:
    print(f'you werent even close dog, it was {actual_sentence}')


def game_loop():
  while True:
    calculator(first_names, last_names, crimes_sentences)


def main():
  game_loop()


if __name__ == "__main__":
  main()
