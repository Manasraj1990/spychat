from spy_detail import spy,Spy,chatMessage
from steganography.steganography import Steganography
from datetime import datetime
import csv


print'Hello Buddy'
print 'Let\'s get started'

STATUS_MESSAGE=['Galti badi galti engineering ','Busy','pleace only call','Be your self ','Never give-up','Sleeping']
frnd1 = Spy('Naman','Mr.',28,3.9)
frnd2 = Spy('kriti','Ms.',25,3.8)
friends = [frnd1,frnd2]

def load_frnds():
    with open('friends.csv','rb')as frinends_data:
        reader = csv.reader (frinends_data)

        for row in reader:
            frnd = Spy(name=row[0], salutation=row[1], rating=row[2], age=row[3])
            friends.append(frnd)


load_frnds()

def add_status(c_status):
    if c_status != None:
        print 'Your current status is '+ c_status
    else:
        print 'You don\'t have any status currently'
    existing_status = raw_input('You want to select from old status? Y\N')
    if existing_status.upper()== 'N':
        new_status =raw_input('Enter your status :')
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)

    elif existing_status.upper()=='Y':
          serial_no =1
          for old_status in STATUS_MESSAGE:
            print str(serial_no)+'. '+old_status
            serial_no=serial_no + 1
          user_choice= input ('Enter your choice:')
          new_status= STATUS_MESSAGE[user_choice-1]
    updated_status = new_status
    return updated_status

def add_friend():
    frnd =Spy('','',0,0.0)
    frnd.name=raw_input('What is your friend name?-> ')
    frnd.sal=raw_input('what should we call you? ->')
    frnd.age=input('What is your friend age?->')
    frnd.rating =input('What is your friend rating-> ')
    frnd.is_online =True
    if len(frnd.name)>2 and 12<frnd.age<60 and frnd.rating>spy.rating:
       with open('friends.csv','a')as (friends_data):
           writer = csv.writer(friends_data)
           writer.writerow([frnd.name,frnd.sal,frnd.rating,frnd.age,frnd.is_online])

    else:
        print 'Friend cannot be added'
    return len(friends)

def select_frnd():
    serial_no = 1
    for frnd in friends:
        print str(serial_no)+ '. ' +frnd.name
        serial_no = serial_no+1
    user_selected_frnd =input('Enter your choice: ')
    user_selected_frnd_index = user_selected_frnd-1
    return user_selected_frnd_index


def send_message():
    selected_fend = select_frnd()
    original_image = raw_input('What is the name of your image?')
    secret_text = raw_input('What is your secret text?')
    output_path = 'output.jpg'
    Steganography.encode(original_image,output_path,secret_text)
    print 'message encoded'
    new_chat =chatMessage(secret_text,True)
    friends[selected_fend].chat.append(new_chat)
    print 'Your secret massage is ready!'

def read_message():
    selected_fend = select_frnd()
    output_path = raw_input('Which image you want to decode?')
    secret_text = Steganography.decode(output_path)
    print 'Secret text is ' + secret_text
    new_chat= chatMessage(secret_text,False)

    friends[selected_fend].chat.append(new_chat)
    print 'your secret message has been saved!'

def start_chat(spy_name,spy_age,spy_rating):
    print 'Here are you options '+spy_name
    current_status =None
    show_menu =True

    while show_menu:
        choice= input('what do you want to do ? \n 1. Add a status \n 2.Add a friend \n 3. send a message\n 4. Read a message \n 0.Exit\n')
        if choice ==1:
            current_status = add_status(current_status)
            print 'Updated status is ' + current_status
        elif choice==2:
            no_of_frnds = add_friend()
            print 'You have '+ str(no_of_frnds ) +' friends'
        elif choice == 3:
            send_message()
        elif choice == 4:
            read_message()
        elif choice == 0:
            show_menu = False
        else:
            print 'invalid input'

spy_exist = raw_input('Are u new user? Y/N: ')
if spy_exist.upper()=='N':
     print 'Welcome back ' +spy.name +' age: ' + str(spy.age) + ' having rating of '+str(spy.rating)
     start_chat(spy.name,spy.age,spy.rating)

elif spy_exist.upper()=='Y':
    spy=Spy('','',0,0.0)
    spy.name = raw_input('What is your spy name? ')
    if spy.name.isalpha()== False:
       print ' Please enter your name'
       exit(0)

    elif len(spy.name) > 2:
       print 'welcome '+ spy.name + ' glad to have you back with us .'
       spy_salutation =raw_input ( 'what should we call you (Mr. or Ms.)?')
       if spy_salutation == 'Mr.' or  spy_salutation == 'Ms.':
         spy.name = spy_salutation + ' ' + spy.name
         print 'Alright, ' + spy.name + ' I would like to know a little bit more about you.'
         spy.age= input ('what is your age ')
         if 60 >= spy.age >12:
             print 'your age is correct'
             spy.rating = input('what is your rating ')
             if spy.rating >5.0:
                 print 'Great spy'
             elif 4.0<= spy.rating <=5.0:
                 print 'Average spy'
             elif 2.0 == spy.rating <3.0:
                 print 'Bad spy'
             else:
                 print 'who hired you?'

                 spy_is_online = True
                 print 'Authentication complete. Welcome ' + spy.name +  ' age : ' +str(spy.age) +' and rating of: '+str(spy.rating) +' proud to have you onboard. '
                 start_chat(spy.name,spy.age,spy.rating)
         else:
             print 'your are not eligible to be a spy '
       else:
           print  'invalid input'
    else:
        print 'Ooops!'

else:
    print' invalid input'