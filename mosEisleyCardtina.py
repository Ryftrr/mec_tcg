'''
gen cohen, connor ciccone, nick barnes, ryan cole
card game
hackNA
'''

import pygame, sys, math, random, time

#Initializing game engine
pygame.init()
pygame.mixer.init()

#Set up drawing surface
w = 800
h = 600
size = (w,h)
surface = pygame.display.set_mode(size)

#Set window title bar
pygame.display.set_caption("'We don't serve their kind here.'")

#Color Constants
WHITE     = (255,255,255)
BLACK     = (  0,  0,  0)
RED       = (255,  0,  0)
GREEN     = (  0,255,  0)
BLUE      = (  0,  0,255)
DARKGREEN = ( 25,105,  0)
#use rectangle objects to identify player class choices
CLONE = pygame.Rect(   w/21, h/2, 4*w/21, h/4)
DROID = pygame.Rect( 6*w/21, h/2, 4*w/21, h/4)
SITH  = pygame.Rect(11*w/21, h/2, 4*w/21, h/4)
JEDI  = pygame.Rect(16*w/21, h/2, 4*w/21, h/4)
HANDPOS1 = pygame.Rect( 6*w/31, 3*h/4, 4*w/31,h/4/1.5)
HANDPOS2 = pygame.Rect(11*w/31, 3*h/4, 4*w/31,h/4/1.5)
HANDPOS3 = pygame.Rect(16*w/31, 3*h/4, 4*w/31,h/4/1.5)
HANDPOS4 = pygame.Rect(21*w/31, 3*h/4, 4*w/31,h/4/1.5)
HANDPOS5 = pygame.Rect(26*w/31, 3*h/4, 4*w/31,h/4/1.5)
PLAYPOS1 = pygame.Rect(6*w/31 , 2*h/4, 4*w/31,h/4/1.5)
PLAYPOS2 = pygame.Rect(11*w/31, 2*h/4, 4*w/31,h/4/1.5)
PLAYPOS3 = pygame.Rect(16*w/31, 2*h/4, 4*w/31,h/4/1.5)
PLAYPOS4 = pygame.Rect(21*w/31, 2*h/4, 4*w/31,h/4/1.5)
PLAYPOS5 = pygame.Rect(26*w/31, 2*h/4, 4*w/31,h/4/1.5)
#defining images

#templatePic = pygame.image.load("Template.png")
#templatePic = pygame.transform.scale(templatePic, (int(4*w/31),int(h/4/1.5)))

theme = pygame.mixer.Sound('mecTheme.ogg')

clonePic  = pygame.image.load("obiwan_profile.png" )
droidPic  = pygame.image.load("gengrev_profile.png")
jediPic   = pygame.image.load("luke_profile.png"   )
sithPic   = pygame.image.load("vader_profile.png"  )
clonePic = pygame.transform.scale(clonePic,[int(4*w/31),int(h/4)])
droidPic = pygame.transform.scale(droidPic,[int(4*w/31),int(h/4)])
jediPic  = pygame.transform.scale(jediPic ,[int(4*w/31),int(h/4)])
sithPic  = pygame.transform.scale(sithPic ,[int(4*w/31),int(h/4)])


#initializes decks for player (eventually for AI)
def initDeck(playerclass):
        
        # format of list is in [picname, attack, health, force cost, status (hand position or position on field),attack status]
        droid1  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid2  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid3  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid4  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid5  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid6  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid7  = ["BATTLEDROID.png"    , 1, 1, 0, "deck", "na"]
        droid8  = ["SUPERBD.png"        , 3, 3, 3, "deck", "na"]
        droid9  = ["SUPERBD.png"        , 3, 3, 3, "deck", "na"]
        droid10 = ["DROIDEKA.png"       , 5, 1, 4, "deck", "na"]
        droid11 = ["DROIDEKA.png"       , 5, 1, 4, "deck", "na"]
        droid12 = ["DROIDEKA.png"       , 5, 1, 4, "deck", "na"]
        droid13 = ["IG88.png"           , 4, 4, 6, "deck", "na"]
        droid14 = ["IG88.png"           , 4, 4, 6, "deck", "na"]
        droid15 = ["JANGOFETT.png"      , 7, 5, 8, "deck", "na"]
        droid16 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        droid17 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        droid18 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        droid19 = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        droid20 = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]

        clone1  = ["CLONETROOPER.png"   , 3, 1, 3, "deck", "na"]
        clone2  = ["CLONETROOPER.png"   , 3, 1, 3, "deck", "na"]
        clone3  = ["CLONETROOPER.png"   , 3, 1, 3, "deck", "na"]
        clone4  = ["CLONETROOPER.png"   , 3, 1, 3, "deck", "na"]
        clone5  = ["CLONETROOPER.png"   , 3, 1, 3, "deck", "na"]
        clone6  = ["ROYAL GUARDS.png"   , 2, 3, 3, "deck", "na"]
        clone7  = ["ROYAL GUARDS.png"   , 2, 3, 3, "deck", "na"]
        clone8  = ["ROYAL GUARDS.png"   , 2, 3, 3, "deck", "na"]
        clone9  = ["ROYAL GUARDS.png"   , 2, 3, 3, "deck", "na"]
        clone10 = ["ATTE.png"           , 3, 3, 3, "deck", "na"]
        clone11 = ["ATTE.png"           , 3, 3, 3, "deck", "na"]
        clone12 = ["ATTE.png"           , 3, 3, 3, "deck", "na"]
        clone13 = ["COMMANDERCODY.png"  , 4, 3, 5, "deck", "na"]
        clone14 = ["COMMANDERCODY.png"  , 4, 3, 5, "deck", "na"]
        clone15 = ["PADME.png"          , 7, 4, 7, "deck", "na"]
        clone16 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        clone17 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        clone18 = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        clone19 = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        clone20 = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]

        jedi1   = ["REBELTROOPER.png"   , 1, 3, 1, "deck", "na"]
        jedi2   = ["REBELTROOPER.png"   , 1, 3, 1, "deck", "na"]
        jedi3   = ["REBELTROOPER.png"   , 1, 3, 1, "deck", "na"]
        jedi4   = ["REBELTROOPER.png"   , 1, 3, 1, "deck", "na"]
        jedi5   = ["REBELTROOPER.png"   , 1, 3, 1, "deck", "na"]
        jedi6   = ["REBELPILOT.png"     , 3, 2, 3, "deck", "na"]
        jedi7   = ["REBELPILOT.png"     , 3, 2, 3, "deck", "na"]
        jedi8   = ["REBELPILOT.png"     , 3, 2, 3, "deck", "na"]
        jedi9   = ["XWING.png"          , 5, 2, 4, "deck", "na"]
        jedi10  = ["XWING.png"          , 5, 2, 4, "deck", "na"]
        jedi11  = ["PRINCESSLEIA.png"   , 6, 4, 8, "deck", "na"]
        jedi12  = ["PRINCESSLEIA.png"   , 6, 4, 8, "deck", "na"]
        jedi13  = ["HANSOLO.png"        , 6, 4, 8, "deck", "na"]
        jedi14  = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        jedi15  = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        jedi16  = ["TUSKENRAIDER.png"   , 2, 1, 2, "deck", "na"]
        jedi17  = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        jedi18  = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        jedi19  = ["LANDSPEEDER.png"    , 3, 1, 2, "deck", "na"]
        jedi20  = ["LANDSPEEDER.png"    , 3, 1, 2, "deck", "na"]

        sith1   = ["STORMTROOPER.png"   , 2, 2, 1, "deck", "na"]
        sith2   = ["STORMTROOPER.png"   , 2, 2, 1, "deck", "na"]
        sith3   = ["STORMTROOPER.png"   , 2, 2, 1, "deck", "na"]
        sith4   = ["STORMTROOPER.png"   , 2, 2, 1, "deck", "na"]
        sith5   = ["STORMTROOPER.png"   , 2, 2, 1, "deck", "na"]
        sith6   = ["SANDTROOPER.png"    , 2, 3, 2, "deck", "na"]
        sith7   = ["SANDTROOPER.png"    , 2, 3, 2, "deck", "na"]
        sith8   = ["SANDTROOPER.png"    , 2, 3, 2, "deck", "na"]
        sith9   = ["SANDTROOPER.png"    , 2, 3, 2, "deck", "na"]
        sith10  = ["SANDTROOPER.png"    , 2, 3, 2, "deck", "na"]
        sith11  = ["ATST.png"           , 2, 3, 4, "deck", "na"]
        sith12  = ["ATST.png"           , 2, 3, 4, "deck", "na"]
        sith13  = ["BOBAFETT.png"       , 5, 3, 5, "deck", "na"]
        sith14  = ["BOBAFETT.png"       , 5, 3, 5, "deck", "na"]
        sith15  = ["PALPATINE.png"      , 5, 7, 7, "deck", "na"]
        sith16  = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        sith17  = ["JARJARBINK.png"     , 1, 5, 4, "deck", "na"]
        sith18  = ["RANCOR.png"         , 6, 5, 7, "deck", "na"]
        sith19  = ["RANCOR.png"         , 6, 5, 7, "deck", "na"]
        sith20  = ["LANDSPEEDER.png"    , 3, 1, 2, "deck", "na"]
        
        if playerclass == "Droid":
                cardlist = [droid1,droid2,droid3,droid4,droid5,droid6,droid7,droid8,droid9,droid10,droid11,droid12,droid13,droid14,droid15,droid16,droid17,droid18,droid19,droid20]
        elif playerclass == "Clone":
                cardlist = [clone1,clone2,clone3,clone4,clone5,clone6,clone7,clone8,clone9,clone10,clone11,clone12,clone13,clone14,clone15,clone16,clone17,clone18,clone19,clone20]
        elif playerclass == "Jedi":
                cardlist = [ jedi1, jedi2, jedi3, jedi4, jedi5, jedi6, jedi7, jedi8, jedi9, jedi10, jedi11, jedi12, jedi13, jedi14, jedi15, jedi16, jedi17, jedi18, jedi19, jedi20]
        elif playerclass == "Sith":
                cardlist = [ sith1, sith2, sith3, sith4, sith5, sith6, sith7, sith8, sith9, sith10, sith11, sith12, sith13, sith14, sith15, sith16, sith17, sith18, sith19, sith20]
        return cardlist
#retrieves starting hand and defines what the new cardlist is once the deck loses the cards it draws
def getAttackValue(atk, hp):
        hp -= atk
        return hp

#displays the cards that are played on the surface
def drawPlayedCards(playedCards):
        if playedCards[0] != "":
                card1 = playedCards[0]
                image1= pygame.image.load(card1[0])
                image1 = pygame.transform.scale(image1, (int(4*w/31),int(2*h/11)))
                surface.blit(image1, (6*w/31, 2*h/4))
                getStats(card1[1],card1[2],card1[3],6*w/31,2*h/4)
        if playedCards[1] != "":
                print(1)
                card2 = playedCards[1]
                image2= pygame.image.load(card2[0])
                image2 = pygame.transform.scale(image2, (int(4*w/31),int(2*h/11)))
                surface.blit(image2, (11*w/31, 2*h/4))
                getStats(card2[1],card2[2],card2[3],11*w/31,2*h/4)
        if playedCards[2] != "":
                card3 = playedCards[2]
                image3= pygame.image.load(card3[0])
                image3 = pygame.transform.scale(image3, (int(4*w/31),int(2*h/11)))
                surface.blit(image3, (16*w/31, 2*h/4))
                getStats(card3[1],card3[2],card3[3],16*w/31,2*h/4)
        if playedCards[3] != "":
                card4 = playedCards[3]
                image4= pygame.image.load(card4[0])
                image4 = pygame.transform.scale(image4, (int(4*w/31),int(2*h/11)))
                surface.blit(image4, (21*w/31, 2*h/4))
                getStats(card4[1],card4[2],card4[3],21*w/31,2*h/4)
        if playedCards[4] != "":
                card5 = playedCards[4]
                image5= pygame.image.load(card5[0])
                image5 = pygame.transform.scale(image5, (int(4*w/31),int(2*h/11)))
                surface.blit(image5, (26*w/31, 2*h/4)) 
                getStats(card5[1],card5[2],card5[3],26*w/31,2*h/4)
def startHand(cardlist):
        hand = ["", "", "", "", ""]
        hand[0]= drawCard(cardlist)
        hand[1]= drawCard(cardlist)
        hand[2]= drawCard(cardlist)
        return hand
'''
draw the game screen for when the game starts
'''        
def initGameScreen(hand,playerClass,aiClass,classPic):
   
        drawHand(hand,classPic)
    

#draws hand of player and AI
def drawHand(hand,classPic):
        #draw you hero pic
        surface.blit(classPic, [w/31,3*h/4])
        #draw your hand
        if(hand[0] != ""):

                card1 = hand[0]
                image1 = pygame.image.load(card1[0])
                image1 = pygame.transform.scale(image1, (int(4*w/31),int(2*h/11)))
                surface.blit(image1, (6*w/31, 3*h/4))
                getStats(card1[1], card1[2], card1[3], 6*w/31,3*h/4)
                
        if(hand[1] != ""):
                card2 = hand[1]
                image2= pygame.image.load(card2[0])
                image2 = pygame.transform.scale(image2, (int(4*w/31),int(2*h/11)))
                surface.blit(image2, (11 * w/31, 3*h/4))
                getStats(card2[1], card2[2], card2[3], 11*w/31,3*h/4)
                
        if(hand[2] != ""):
                card3 = hand[2]
                image3= pygame.image.load(card3[0])
                image3 = pygame.transform.scale(image3, (int(4*w/31),int(2*h/11)))
                surface.blit(image3, (16 * w/31, 3*h/4))
                getStats(card3[1], card3[2], card3[3], 16*w/31,3*h/4)
        if(hand[3] != ""):
                card4 = hand[3]
                image4= pygame.image.load(card4[0])
                image4 = pygame.transform.scale(image4, (int(4*w/31),int(2*h/11)))
                surface.blit(image4, (21 * w/31, 3*h/4))  
                getStats(card4[1], card4[2], card4[3], 21*w/31,3*h/4)
        if(hand[4] != ""):
                card5 = hand[4]
                image5= pygame.image.load(card5[0])
                image5 = pygame.transform.scale(image5, (int(4*w/31),int(2*h/11)))
                surface.blit(image5, (26 * w/31, 3*h/4))   
                getStats(card5[1], card5[2], card5[3], 26*w/31,3*h/4)
                
        #draw ai hand
        pygame.draw.rect(surface,RED,(w/31,h/4-h/4/2,4*w/31,h/4/2),0)
        pygame.draw.rect(surface,BLUE,(6*w/31,h/4 - h/4/1.5,4*w/31,h/4/1.5),0)
        pygame.draw.rect(surface,BLUE,(11*w/31,h/4- h/4/1.5,4*w/31,h/4/1.5),0)
        pygame.draw.rect(surface,BLUE,(16*w/31,h/4 - h/4/1.5,4*w/31,h/4/1.5),0)
        pygame.draw.rect(surface,BLUE,(21*w/31,h/4 - h/4/1.5,4*w/31,h/4/1.5),0)
        pygame.draw.rect(surface,BLUE,(26*w/31,h/4 - h/4/1.5,4*w/31,h/4/1.5),0)           

#function spawns the intro screen. Later will implement a game in or not in play variable to determine when it spawns the intro screen
def initClassScreen():
    
    introtext, textbounds = showMessage("Mos Eisley Cantina TCG", "Consolas", 30, w/2, h/10, BLACK)
    classtext, classbounds = showMessage("Choose Your Class", "Consolas", 25, w/2, h/5, BLACK)
    surface.blit(droidPic,DROID)
    surface.blit(clonePic,CLONE)
    surface.blit(jediPic , JEDI)
    surface.blit(sithPic , SITH)
    surface.blit(introtext, textbounds)
    surface.blit(classtext, classbounds)
'''
draw card given the potential list for the class
'''
def drawCard(cardlist):
    cardnum = random.randint(0,19)
    card = cardlist[cardnum]
    #del cardlist[cardnum]
    return card
def showMessage(words, fontName, size, xVal, yVal, forecolor, bg=None):
    font = pygame.font.SysFont(fontName, size, 0, 0)
    text = font.render(words, True, forecolor, bg)
    #get rectangle bounding box of text
    textbounds = text.get_rect()
    #centering
    textbounds.center = (xVal, yVal)
    #update to screen
    return text, textbounds

#accepts a card and the force
#return true or false, true for enough force, false for not enough
def checkForce(card, forceLeft):
        forceCost = card[3]
        if(forceLeft >= forceCost):
                return True
        elif(forceLeft < forceCost):
                return False
        
        #blits tha stats to the screen with the card
def getStats(attack, health, force, x,y):
        atk = str(attack)
        hp = str(health)
        fr = str(force)
        text,textBounds = showMessage(atk + "/" + hp, "Consolas", 16, x+8,y+100, WHITE, BLACK)
        text2, textBounds2 = showMessage(fr, "Consolas", 16, x, y ,WHITE,BLACK)
        surface.blit(text,textBounds)
        surface.blit(text2, textBounds2)
#when the player clicks the end turn button
#accepts turn count, force count, cardlist, hand
#returns turn count, force count, cardlist, hand
def endTurn(turncount, forceCount, cardlist, hand, playerCardsInPlay):
        if turncount < 8: #turn and force count go up by one
                turncount += 1
                forceCount += 1
                gameInPlay = True
                
                if(playerCardsInPlay[0] !=""):
                        card1 = playerCardsInPlay[0]
                        card1[4] ="not attacking"
                if(playerCardsInPlay[1] !=""):
                        card2 = playerCardsInPlay[1]
                        card2[4] ="not attacking"
                if(playerCardsInPlay[2] !=""):
                        card3 = playerCardsInPlay[2]
                        card3[4] ="not attacking" 
                if(playerCardsInPlay[3] !=""):
                        card4 = playerCardsInPlay[3]
                        card4[4] ="not attacking" 
                if(playerCardsInPlay[4] !=""):
                        card5 = playerCardsInPlay[4]
                        card5[4] ="not attacking"
                        
        elif turncount >= 8:
                turncount = 8
                forceCount = 8
                gameInPlay = True
                
                return turncount, forceCount, cardlist, hand, gameInPlay, playerCardsInPlay
                             
                
        elif turncount >= 8:
                losstext, lossbounds = showMessage("You Lose. Click to Continue", "Consolas", 25, w/2,h/2,RED)
                surface.blit(losstext, lossbounds)
                time.sleep(3)
                gameInPlay = False
                
                
        if(hand[0]== ""):
                card = drawCard(cardlist)
                hand[0] =card
        elif(hand[1] == ""):
                card = drawCard(cardlist)
                hand[1] = card
        elif(hand[2] == ""):
                card = drawCard(cardlist)
                hand[2] = card
        elif(hand[3] == ""):
                card = drawCard(cardlist)
                hand[3] = card
        elif(hand[4] == ""):
                card = drawCard(cardlist)
                hand[4] = card
        
   
        return turncount, forceCount, cardlist, hand, gameInPlay, playerCardsInPlay

def playCard(playerCardsInPlay, forceCount, hand):
        for event in pygame.event.get():
                if(HANDPOS1.collidepoint(pygame.mouse.get_pos())):#if they click on the first positon of the hand
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                forceLeft = checkForce(hand[0], forceCount)
                                if(forceLeft): #if they have enough force to play the card
                                        if(playerCardsInPlay[0] == ""): #if the first spot is empty, put it in there
                                                playerCardsInPlay[0] = (hand[0])
                                                card = hand[0]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[0] = ""                                                
                                        elif(playerCardsInPlay[1] == ""):
                                                playerCardsInPlay[1] = hand[0]
                                                card = hand[0]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[0] = ""                                                
                                        elif(playerCardsInPlay[2] == ""):
                                                playerCardsInPlay[2] = hand[0]
                                                card = hand[0]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[0] = ""                                                
                                        elif(playerCardsInPlay[3] == ""):
                                                playerCardsInPlay[3] = hand[0] 
                                                card = hand[0]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[0] = ""                                                
                                        elif(playerCardsInPlay[4] == ""):
                                                playerCardsInPlay[4] = hand[0]
                                                card = hand[0]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[0] = ""
        
                                                
                                        
                                        
                if(HANDPOS2.collidepoint(pygame.mouse.get_pos())):#if they click on the second positon of the hand
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                forceLeft = checkForce(hand[1], forceCount)
                                if(forceLeft): #if they have enough force to play the card
                                        if(playerCardsInPlay[0] == ""): #if the first spot is empty, put it in there
                                                playerCardsInPlay[0] = (hand[1])
                                                card = hand[1]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[1] = ""                                                
                                        elif(playerCardsInPlay[1] == ""):
                                                playerCardsInPlay[1] = hand[1]
                                                card = hand[1]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[1] = ""                                                
                                        elif(playerCardsInPlay[2] == ""):
                                                playerCardsInPlay[2] = hand[1]
                                                card = hand[1]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[1] = ""                                                
                                        elif(playerCardsInPlay[3] == ""):
                                                playerCardsInPlay[3] = hand[1] 
                                                card = hand[1]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[1] = ""                                                
                                        elif(playerCardsInPlay[4] == ""):
                                                playerCardsInPlay[4] = hand[1]
                                                card = hand[1]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[1] = ""                                                
                                          
                                        
                if(HANDPOS3.collidepoint(pygame.mouse.get_pos())):#if they click on the third positon of the hand
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                forceLeft = checkForce(hand[2], forceCount)
                                if(forceLeft): #if they have enough force to play the card
                                        if(playerCardsInPlay[0] == ""): #if the first spot is empty, put it in there
                                                playerCardsInPlay[0] = (hand[2])
                                                card = hand[2]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[2] = "" #remove card from hand                                                
                                        elif(playerCardsInPlay[1] == ""):
                                                playerCardsInPlay[1] = hand[2]
                                                card = hand[2]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[2] = "" #remove card from hand                                                
                                        elif(playerCardsInPlay[2] == ""):
                                                playerCardsInPlay[2] = hand[2]
                                                card = hand[2]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[2] = "" #remove card from hand                                                
                                        elif(playerCardsInPlay[3] == ""):
                                                playerCardsInPlay[3] = hand[2] 
                                                card = hand[2]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[2] = "" #remove card from hand                                                
                                        elif(playerCardsInPlay[4] == ""):
                                                playerCardsInPlay[4] = hand[2]
                                                card = hand[2]
                                                forceCount -= card[3] #subtract force                                         
                                                hand[2] = "" #remove card from hand                                                
                                        
                if(HANDPOS4.collidepoint(pygame.mouse.get_pos())):#if they click on the fourth positon of the hand
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                forceLeft = checkForce(hand[3], forceCount)
                                if(forceLeft): #if they have enough force to play the card
                                        if(playerCardsInPlay[0] == ""): #if the first spot is empty, put it in there
                                                playerCardsInPlay[0] = (hand[3])
                                                card = hand[3]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[3] = ""                                                
                                        elif(playerCardsInPlay[1] == ""):
                                                
                                                playerCardsInPlay[1] = hand[3]
                                                card = hand[3]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[3] = ""                                                
                                        elif(playerCardsInPlay[2] == ""):
                                                playerCardsInPlay[2] = hand[3]
                                                card = hand[3]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[3] = ""                                                
                                        elif(playerCardsInPlay[3] == ""):
                                                playerCardsInPlay[3] = hand[3] 
                                                card = hand[3]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[3] = ""                                                
                                        elif(playerCardsInPlay[4] == ""):
                                                playerCardsInPlay[4] = hand[3] 
                                                card = hand[3]
                                                forceCount -= card[3] #subtract force                                        
                                                hand[3] = ""                                                
                                        
                if(HANDPOS5.collidepoint(pygame.mouse.get_pos())):#if they click on the fifth positon of the hand
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                forceLeft = checkForce(hand[4], forceCount)
                                if(forceLeft): #if they have enough force to play the card
                                        if(playerCardsInPlay[0] == ""): #if the first spot is empty, put it in there
                                                playerCardsInPlay[0] = (hand[4])
                                                card = hand[4]
                                                forceCount -= card[3] #subtract force
                                                hand[4] = ""                                                
                                        elif(playerCardsInPlay[1] == ""):
                                                playerCardsInPlay[1] = hand[4]
                                                card = hand[4]
                                                forceCount -= card[3] #subtract force
                                                hand[4] = ""                                                
                                        elif(playerCardsInPlay[2] == ""):
                                                playerCardsInPlay[2] = hand[4]
                                                card = hand[4]
                                                forceCount -= card[3] #subtract force
                                                hand[4] = ""                                                
                                        elif(playerCardsInPlay[3] == ""):
                                                playerCardsInPlay[3] = hand[4]
                                                card = hand[4]
                                                forceCount -= card[3] #subtract force
                                                hand[4] = ""                                                
                                        elif(playerCardsInPlay[4] == ""):
                                                playerCardsInPlay[4] = hand[4] 
                                                card = hand[4]
                                                forceCount -= card[3] #subtract force
                                                hand[4] = ""
                return playerCardsInPlay, forceCount

def attackSeq(AIhealth, playerCardsInPlay):
        if(PLAYPOS1.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[0] ==""):#if there is a card there
                                card = playerCardsInPlay[0]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack

        if(PLAYPOS2.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[1] ==""):#if there is a card there
                                card = playerCardsInPlay[1]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack   

        if(PLAYPOS3.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[2] ==""):#if there is a card there
                                card = playerCardsInPlay[2]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack  

        if(PLAYPOS3.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[3] ==""):#if there is a card there
                                card = playerCardsInPlay[3]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack  
        if(PLAYPOS4.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[4] ==""):#if there is a card there
                                card = playerCardsInPlay[4]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack 
        if(PLAYPOS5.collidepoint(pygame.mouse.get_pos())):
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):                                                       
                        if(playerCardsInPlay[5] ==""):#if there is a card there
                                card = playerCardsInPlay[5]
                                if(card[5] == "na"): #if they havent attackedf yet
                                        card[5] = "ak"
                                        attack = card[1]
                                        AIhealth -= attack        
        return AIhealth

def main():
    #setting initial playerClass = empty so that we don't get an error due to reference before assignment.
    playerclass = ""
    classPic = ""
    gameInPlay = False
    text, textbounds =showMessage(" End Turn ", "Consolas", 20, w/8, 2 *h/3, GREEN, BLACK)
    turncount = 0
    forceCount = 1
    playerHealth = 30
    AIhealth = 30
    playerCardsInPlay = ["","","","",""]
    #when game isn't in play it instantiates the class screen

    while(True):
        pygame.mixer.Sound.play(theme,-1,0,0)
        for event in pygame.event.get():
                if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                        pygame.quit()
                        sys.exit()
            #mouse collision detection
                if DROID.collidepoint(pygame.mouse.get_pos()):
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                                playerclass = "Droid"
                                classPic    =  droidPic
                                gameInPlay = True
                                cardlist = initDeck(playerclass)
                                hand=  startHand(cardlist)
                        #also init game screen and init game 
                elif CLONE.collidepoint(pygame.mouse.get_pos()):
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                                playerclass = "Clone"
                                classPic    =  clonePic
                                gameInPlay = True
                                cardlist = initDeck(playerclass)
                                hand =  startHand(cardlist)
                elif SITH.collidepoint(pygame.mouse.get_pos()):
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):                
                                playerclass = "Sith"
                                classPic    =  sithPic
                                gameInPlay = True
                                cardlist = initDeck(playerclass)
                                hand =  startHand(cardlist)
                elif JEDI.collidepoint(pygame.mouse.get_pos()):
                        if(event.type == pygame.MOUSEBUTTONDOWN and event.button ==1):
                                playerclass = "Jedi"
                                classPic    =  jediPic
                                gameInPlay = True
                                cardlist = initDeck(playerclass)
                                hand =  startHand(cardlist)
               
               
                            
                           
                                
                
        #Set Background Fill
        surface.fill(WHITE)
        
        #Drawing code goes here
        if gameInPlay == False:
                initClassScreen()
        #when game is in play it spawns the game screen.
        if gameInPlay:
                        initGameScreen(hand,playerclass, "hi", classPic) 
                        surface.blit(text, textbounds)
                        drawPlayedCards(playerCardsInPlay)
                        forceText, forceTextBounds = showMessage(str(forceCount), "Consolas", 20, w/31 + 2 * w/31,2*h/4 + h/16, BLACK)
                        #surface.blit(healthText, healthTextBounds)
                        surface.blit(forceText, forceTextBounds)
                        #if they press on the first play area spot   
        
                        #if end turn button hit
                        if textbounds.collidepoint(pygame.mouse.get_pos()): 
                                if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                                        turncount, forceCount, cardlist, hand, gameInPlay, playerCardsInPlay = endTurn(turncount,forceCount,cardlist, hand, playerCardsInPlay)   
                                
                        #check if they click on a card in their hand, remove it from their hand, subtract force, and put in on the playing field
                        playerCardsInplay, forceCount = playCard(playerCardsInPlay, forceCount, hand)                                             
                        #AIhealth = attackSeq(AIhealth, playerCardsInPlay)                      
                                                
       
        pygame.display.update()
main()