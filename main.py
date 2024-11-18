
#1
list_of_names= ["Attila", "Zarya", "Starship", "Ilon", "Gooder"]
false_answer="Тут ничего нет. Еще есть вопросы?"
def concatinate_true_string(input_string):
    return f"Ты – свой. Приветствую, любезный {input_string}!"
def welcome_quest():
    name= input("Ввше имя:")
    if name in list_of_names:
        print(concatinate_true_string(name))
        return
    elif name =='':
        return
    else:
        print(false_answer)
              
# welcome_quest()

#2
def greeting_guest():
    name = input("как вас зовут?")
    print(f'Здравствуйте {name}')
    print("как дела?")
    print("1. Хорошо")
    print("2. Плохо")
    mood = input()
    if (mood == "1" or mood == "Хорошо" or mood=="хорошо"):
        print("Я рад за вас")
        return 
    elif (mood == "2" or mood == "Плохо" or mood=="плохо"):
        print("Мне жаль")
        return
    else:
        print("Invalid choice. Please try again.")



greeting_guest()