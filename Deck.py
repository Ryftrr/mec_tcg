'''
Mos Eisley Cardtina Project (Deck Object Class)
'''

#Version Alpha 1.1.2
'''
class Deck:
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
    
    def startHand(cardlist):
        hand = ["", "", "", "", ""]
        hand[0]= drawCard(cardlist)
        hand[1]= drawCard(cardlist)
        hand[2]= drawCard(cardlist)
        return hand
    
'''
