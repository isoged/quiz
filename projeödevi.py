def new_game():##fonksiyonumuz kuruyoruz##

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Cevap : ")#kullanıcı cevap girmesi için yazılmıştır.
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

#doğru yada yannış komutları 
def check_answer(answer, guess):

    if answer == guess:#eğer kullanıcı doğru işaretlerse 1 yanlış işaretlerse 0 (bildiği soru sayısı),if else komutları kullanılmıştır.
        print("Doğru!")
        return 1
    else:
        print("Yanlış!")
        return 0
