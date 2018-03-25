print'Hello Buddy'
print 'let\'s get started'
spy_name = raw_input('what is your spy name? ')
if len(spy_name) > 2:
   print 'welcome '+ spy_name + ' glad to have you back with us .'
   spy_salutation =raw_input( 'what should we call you (Mr. or Ms.)?')
   if spy_salutation == 'Mr.' or  spy_salutation == 'Ms.':
     spy_name = spy_salutation + ' ' + spy_name
     print 'Alright, ' + spy_name + ' I would like to know a little bit more about you.'
     spy_age= input ('what is your age ')
     if 60 >= spy_age >12:
         print 'your age is correct'
         spy_rating = input('what is your rating ')
         if spy_rating >5.0:
             print 'Great spy'
         elif 4.0<= spy_rating <=5.0:
             print 'Average spy'
         elif 2.0 == spy_rating <=3.0:
             print 'Bad spy'
         else:
             print 'who hired you?'
             spy_is_online = True
             print 'Authentication complete. Welcome ' +spy_name+  ' age : ' +str(spy_age) +' and rating of: '+ str(spy_rating) +' proud to have you onboard'
     else:
         print 'your are not eligible to be a spy '
   else:
       print  'invalid input'
else:

    print 'Ooops!'