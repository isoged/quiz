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

#puanlama için için yazılmışır 
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("SONUÇLAR")
    print("-------------------------")

    print("Senin Cevapların: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Cevap Anahtarı: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Puan: "+str(score)+"")

#oyunun başa dönemesini için yazılmıştır 
def play_again():

    response = input("Başa dönmek istiyor musun ? (Evet ya da Hayır): ")
    response = response.upper()

    if response == "Evet":
        return True
    else:
        return False
# -------------------------

#Aşağıda sorular ve cevapları var.
questions = {
 "1 - Aşağıdakilerden hangisi Yemek Sodası'dır ?: ": "B",
 "2 - Aşağıdakilerden hangisi HNO3 anlamına gelir ?: ": "A",
 "3 - Aşağıdakilerden hangisi Su'dur ?: ": "D",
 "4 - Aşağıdakilerden hangisi Sönmüş Kireç'tir ?: ": "C",
 "5 - Aşağıdakilerden hangisi Na2SO4 anlamına gelir ?: ": "A",
 "6 - Aşağıdakilerden hangisi N2O5 anlamına gelir ?: ": "B",
 "7 - Aşağıdakilerden hangisi Sodyum Klorür'dür ?: ": "D",
 "8 - Aşağıdakilerden hangisi Kalsiyum Sülfat'tır ?: ": "C",
 "9 - Aşağıdakilerden hangisi CuO anlamına gelir ?: ": "B",
 "10 - Aşağıdakilerden hangisi Kalay Sülfür'dür?: ": "A"
}
#Aşağıda soruların seçenekleri var.
options = [["A. CH3COOH", "B. NaHCO3", "C. NaClO", "D. Na2SO4"],
          ["A. Kezzap", "B. Tuz Ruhu", "C. Sönmüş Kireç", "D. Sudkostik"],
          ["A. Nh3", "B. H2SO4 ", "C. NaCl", "D. H2O"],
          ["A. HNO3", "B. CH3COOH", "C. Ca(OH)2", "D. NaClO"],
          ["A. Glauber Tuzu", "B. Çamaşır Suyu", "C. Sirke Asidi", "D. Yemek Sodası"],
          ["A. Fosfor Tri Oksit", "B. Di Azot Penta Oksit", "C. Kalay Sülfür" "D. Karbon Di Oksit"],
          ["A. CuO", "B. Al2O3", "C. PCl" "D. NaCl"],
          ["A. O2", "B. Na2CO3 ", "C. CaSO4" "D. NaHCO3"],
          ["A. Demir Klortür", "B. Bakır Oksit", "C. Demir Klorür" "D. Çinko Oksit"],
          ["A. SnS", "B. FeCl3", "C. CaO" "D. Cu"]]
new_game()

while play_again():
    new_game()

print("Test Tamamlanmıştır")
#uygulamaızda soru ve cevapları değiştirmesi gayet kolaydır.
#mesela bir orta okul öğretmeni öğrencilerine sınav veya quiz yapmak isterse kodlardan kolaylıkla soru ve cevapları değiştirerek yeni quiz veya sınavlar yapabilir.
#uygulamamızda yazılan yazıların neden olduğu kolaylıkla anlaşılabilir.



#not: yazılımların hepsi bize aittir 
