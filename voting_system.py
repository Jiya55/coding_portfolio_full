#election



members= {'jiya':['123456789101', 18, 'hello123']}

#sign up
def sign_up(info):
    name, aadhar_card, age, password=info
    confirm_password = input('confirm password')
    if password==confirm_password:
        if len(aadhar_card)==12:
            if age >=18:
                members[name]=[aadhar_card, age, password]
            else:
                print('You have to be atleast 18 to vote')
        else:
            print('not a real aadhar card')
    else:
        print('password not correct')
def log_in(info):
    name, aadhar_card, age, password=info
    if name in members.keys():
        if len(members[name][0])==12 and len(members[name][0])==aadhar_card:
            if members[name][2]==password:
                print('hello name')
            else:
                print('wrong password')
        else:
            print('wrong aadhar card')
    else:
        print('wrong name')
def ask_info():
    name = input('name: ')
    aadhar_card = input('aadhar_card')
    age = int(input('age: '))
    password= input('password: ')
    return name, aadhar_card , age, password

parties= {'congress':'Sonia gandhi', 'BJP':'Narinder Modi', "Aam Aadmi Party":'Arvind kajeriwal'}
def Print_options():
    for i in parties:
        print(i, '-',parties[i])
Print_options()
votes= {'congress': 50, 'BJP': 25, "aam aadmi party": 70}
def Vote_casting(vote):
    if vote == 'congress':
        votes['congress' ]+=1
        print('1 vote went to congress')
    elif vote == 'BJP':
        votes['BJP' ]+=1
        print('1 vote went to BJP')
    elif vote == 'aam aadmi party':
        votes['aam aadmi party' ]+=1
        print('1 vote went to aam aadmi party')
    else:
        print('no party with that name exists')
Vote_casting('congress')
def winner():
    pass
name= input('name: ')

'''
authenticator for aadhar card
GUI
checking if user has voted or not
notifying user if date to close voting is near(this is advanced)
save data?????
strong password checker
automatically takes aadhar_card and matches data(aadar car will be dictionary thne ad the user doesnt have to check it)
'''


