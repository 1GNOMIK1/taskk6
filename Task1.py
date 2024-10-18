import random
try:
  words=[]
  with open("input01.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
  for item in lines:
     words.append(item.strip())
     a = random.randint(0, len(words)-1)
     secret_world = words[a]
     WORLD= list(secret_world)
     answerArray = ["_"] * len(WORLD)



  print("Угадайте слово: ", ' '.join(answerArray))
  answer=[]
  while answerArray != WORLD:
       letter = input("Введите букву или exit для выхода: ").lower()
       answer.append(letter)
       if letter == 'exit':
           print("Вы закончили игру")
       break
  if len(letter) != 1 or not letter.isalpha() or letter in answer:
      print("Введите повторную букву")

  for i in range (len(WORLD)):
      if WORLD[i] == letter:
          answerArray[i]= letter
  print("Текущее слово: ","".join(answerArray))
  print(f"Угадано букв: {sum(1 for a in answerArray if a != '_')} из {len(WORLD)}")
  if answerArray == WORLD:
      print("Вы угадали словов:", secret_world)




except FileNotFoundError:
  print("Файл не найден.")
