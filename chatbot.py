from time import *
from datetime import *
print("Hello, I am Chatbot")
name = input('And what is your name? ')
sleep(2)
print('hello, ', name)
def task():
    task = input('what do you want to do - Chat, Listen to music(music), Explore fun website(fun), or study(study)').upper()
    tasks = ['STUDY']
    if task == 'CHAT':
        sleep(2)
        chat = input(' What are your hobbies ')
        sleep(2)
        print('i also like ', chat)
        sleep(2)
        chat = input(' what is your favourite color ?')
        sleep(2)
        print('oh, ', chat,' is a very good color')
        sleep(2)
        d, m, y =[int(x) for x in input(' when is your Birthday in this year?(dd/mm/yyyy)').split('/')]
        today = date.today()
        dt = date(y, m, d)
        if dt == today:
            print("Happy birthday")
        else:
            print('i was proggramed on 11.5.2020')
        print(today)
        chat = input(' my battery is low so i better charge bye')
    elif task == 'MUSIC':
        chat = input("What kind of music do you like (R&B, Pop, rap,or Soundtracks) ").upper()
        Chat= input('Let me search my library')
        sleep(5)
        d, m, y =[int(x) for x in input(' when is your Birthday in this year?(dd/mm/yyyy)').split('/')]
        today = date.today()
        dt = date(y, m, d)
        if dt == today:
            print("It's your birthday by kidz bop")
        elif chat == "R&B":
            print(" Girl on Fire by Alicia Keys")
        elif chat =="POP":
            Pop = ['B.E.A.T by L2M', 'Born To Shine by TINI', 'Original(Sia-movie-Dolittle)', 'Try Everything(Shakira)']
            print('these are my favourite picks -')
            for song in Pop:
                print(song)
                sleep(2)
        elif chat =="RAP":
            print('SPIRIT by Beyonce')
        elif chat =="SOUNDTRACKS":
            Pop = ['Speechless (aladin)', 'Better when i am dancing(The peanuts movie)', 'Original(Sia-movie-Dolittle)', 'Just Sing(Trolls world tour)']
            print('these are my favourite picks -')
            for song in Pop:
                print(song)
                sleep(2)
        else:
            print('not a valid answer')
        chat = input(' my battery is low so i better charge bye')
    elif task == 'FUN':
            
            print('these are my picks for fun website ')
            sleep(2)
            websites = ["fun brain", 'cool maths', 'cartoon network']
            print('these are my favourite picks -')
            for website in websites:
                print(website)
                sleep(2)
            chat = input(' my battery is low so i better charge bye')
         
    elif task == 'STUDY':
            
            print('these are my picks for study website ')
            sleep(2)
            websites = ["Khan academy", 'Duolingo', 'scholastic']
            print('these are my favourite picks -')
            for website in websites:
                print(website)
                sleep(2)
            chat = input(' my battery is low so i better charge bye')
    else:
        print('not a valid answer')
            

task()
task()
task()
task()
task()

