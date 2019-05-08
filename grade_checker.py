def calculate_grade(score):
  if score >= 90 and score <= 100:
    return "A+"
  elif score >= 85 and score <= 89:
    return "A"
  elif score >= 80 and score <= 84:
    return "A-"
  elif score >= 77 and score <= 79:
    return "B+"
  elif score >= 73 and score <= 76:
    return "B"
  elif score >= 70 and score <= 72:
    return "B-"
  elif score >= 67 and score <= 69:
    return "C+"
  elif score >= 63 and score <= 66:
    return "C"
  elif score >= 60 and score <= 62:
    return "C-"
  elif score >= 57 and score <= 59:
    return "D+"
  elif score >= 53 and score <= 56:
    return "D"
  elif score >= 50 and score <= 52:
    return "D-"
  elif score >= 0 and score <= 49:
    return "F"
  else:
    return "Sorry, that number is invalid!"

def return_grade():
  print()
  print('------------------------')
  print(f'Your grade is: {calculate_grade(score)}')
  print('------------------------')
  print()


print("What is your grade percentage?")
score = int(input())

return_grade()
