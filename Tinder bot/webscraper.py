from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://tinder.com'
# this struct is just a litst of all the elments that are invloved, There are faster ways but this is a setup this way for keeping it clean and easay to understand
class TinderElements():
    loginButton = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]'
    loginWithPhone = '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]/div/div'
    AcceptLocation = '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]'
    Like = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span'
    Get_tinder_Plus_Notnow = '/html/body/div[2]/main/div/div[3]/button[2]'
    messages_tab = '/html/body/div[1]/div/div[1]/div/aside/nav[2]/div/div/div/div[1]/div/div[2]/button'
    matches_tab = '/html/body/div[1]/div/div[1]/div/aside/nav[2]/div/div/div/div[1]/div/div[1]/button'
    add_tinder_to_home_screen = '/html/body/div[2]/main/div/div[2]/button[2]/div[2]/div[2]'
    serching_bubble = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span[1]'
    messages_index = '/html/body/div[1]/div/div[1]/div/aside/nav[2]/div/div/div/div[2]/div[2]/div[2]/a/div[1]/div/div'
    accept_cookie = '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]'
    allow_location = '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]'
    no_notifcation_button = '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]'
    exit_mesg_button = '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[1]/a/button/svg'

        
############################################################################################################################################################

class TinderBot():
    
    Ele = TinderElements()
    
    def __init__(self):
        self.driver = webdriver.Firefox()

    
    def open_tinder(self):
        self.driver.get(url)

    def accept_cookie_sect(self):
        accept_cookie = self.ifgetele(self.Ele.accept_cookie)
        if accept_cookie == False:
            return
        accept_cookie.click()
        return

    def allow_location(self):
        allow_loc = self.ifgetele(self.Ele.allow_location)
        if allow_loc == False:
            return
        allow_loc.click()
        return 'Location'
        
    #login funfctuion will return a state if it logins will return a state change
    def login(self): 
        loin_action = self.ifgetele(self.Ele.loginButton)
        if loin_action == False:
            return 'opening'
        loin_action.click()
        return 'Login'
    
    def no_notfi(self):
        notfi_button = self.ifgetele(self.Ele.no_notifcation_button)
        if notfi_button == False:
            return
        notfi_button.click()
        return
        
    #basic swip funtion will return a new state if if it has one else it will return nothing 
    def swipe(self):
        #swipe_element = self.ifgetele(self.Ele.Like) /html/body/div[1]/div/div[1]/div/main/div[1]/div/div
        swipe_element = self.ifgetele('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div')
        if swipe_element == False:
            return 'Empty'
        try:
            swipe_element.send_keys(Keys.ARROW_RIGHT)
        except:
            print ('swipe failed')
        print('Swipe')
        return 'Swipping'

    # This function will fetch elements as a array so that we can use empty strings to deduce that we an elmenet is not accesabal it will return the first of the 
    # xpath that we are looking for and will return a false if it found none this will help with the creatation of states and simple prevent crashes and speed devlopment  
    def ifgetele(self, xpath):
        ele = self.driver.find_elements('xpath',xpath)
        if not ele == []:
            return ele[0]
        else:
            return False       

############################################################################################################################################################

class StateMachine():
        CONST_states = {'Location','Login','Swipping','Empty','Questioning'}
        state = 'opening'

        def setstate(self, new_state):
            self.state = new_state
            return

#have not filled this in yet But this willl  be the state machince

############################################################################################################################################################

Bot = TinderBot()
Bot.open_tinder()
State = StateMachine()

############################################################################################################################################################



def Ready():
    print("Program start")
    for i in range(500):
        time.sleep(1)
        Bot.accept_cookie_sect()
        if State.state == 'opening':
            State.setstate(Bot.login())
            print(State.state)
            break
                
    if State.state == 'Login':
        while State.state == 'Login':
            time.sleep(.5)
            if Bot.allow_location() == 'Location':
                State.setstate('Questioning')
                time.sleep(1)
                Bot.no_notfi()
                return    
    quit()

############################################################################################################################################################

Ready()


while 1>0:
    #print(State.state)
    while State.state =='Questioning':
        time.sleep(.5)
        #Out of swipes Mesg
        #send Just match mesg
        #Other Popup that needs to close
        #Look at matches and check to send mesg
        #Check to see if I can repaly to mesg
        #Send back to swip[e loop if nothing to do]
        State.setstate('Swipping') 

    while State.state == 'Swipping':
        time.sleep(.5)
        #out of swipes Mesg
        #Other Popup that needs to close
        #Will check to see if there is a popup or a option to send mesg before swipe 
        should_switch = Bot.swipe()
        if should_switch == 'Empty':
            State.setstate('Questioning')

    if State.state == 'Empty':
        time.sleep(3)
        #sleep for 3 seconds Then go back to question stack
        State.setstate('Questioning')




