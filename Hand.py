class Hand: 
    number_mapping = {
        '1': 14,   '2': 2,  '3': 3, '4': 4,  '5': 5, 
        '6':  6,   '7': 7,  '8': 8, '9': 9, '10': 10, 
        'J': 11,  'Q': 12, 'K': 13, 
    }      
    def __init__(self, cards):
        # check input numbers
        assert len(cards)==5, "length of input is wrong"
        self.cards = cards
        
        self.numbers = []
        self.suits   = []
        for c in self.cards:
            self.numbers = self.numbers + [ c[:-1] ]
            self.suits   = self.suits   + [ c[-1]  ] 

        # check card is right
        assert len( set(self.numbers) - set(list(self.number_mapping)) ) == 0, "card number is wrong"
        assert len( set(self.suits) - set(list(['s', 'h', 'd', 'c'])) )  == 0, "card suit is wrong"
        
        # determine category of value
        self.category = self.card_category()

        # determine value of card
        self.value    = self.calculate_card_value()
    
    def card_category(self):
        # preprocessing
        counts = sorted( [ self.numbers.count(i) for i in self.numbers ],  reverse=True)
        counts_string = ''.join(map(str, counts))
    
        # start to category
        if( counts_string == '44441'): return("full_of_a_kind")
        if( counts_string == '33322'): return("full_house")
        if( counts_string == '33311'): return("three_of_a_kind")
        if( counts_string == '22221'): return("two_pair")
        if( counts_string == '22111'): return("pair")
        
        if( counts_string == '11111'): 
            number = sorted( [self.number_mapping[n] for n in self.numbers],  reverse=True)
            number_string = ''.join(map(str, number)) # for the case 1 2 3 4 5
            diff = max(number) - min(number)
        
            if( len(set(self.suits)) == 1 and (diff == 4 or number_string == '145432')): return("straight_flush")
            if( len(set(self.suits)) == 1 and (diff != 4 or number_string != '145432')): return("flush")    
            if( len(set(self.suits)) != 1 and (diff == 4 or number_string == '145432')): return("straight")    
            if( len(set(self.suits)) != 1 and (diff != 4 or number_string != '145432')): return("high_card")

    def calculate_card_value(self):
        if( self.category == "high_card"       ): return(self.value_high_card()  )
        if( self.category == "pair"            ): return(self.value_pair()       )      
        if( self.category == "two_pair"        ): return(self.value_two_pairs()  )   
        if( self.category == "three_of_a_kind" ): return(self.value_three_of_a_kind() )   
        if( self.category == "straight"        ): return(self.value_straight()   )

        if( self.category == "flush"           ): return(self.value_flush()          )      
        if( self.category == "full_house"      ): return(self.value_full_house()     )   
        if( self.category == "full_of_a_kind"  ): return(self.value_full_of_a_kind() )     
        if( self.category == "straight_flush"  ): return(self.value_straight_flush() )           
                
    def value_high_card(self):
        number = sorted( [self.number_mapping[n] for n in self.numbers],  reverse=True)
        
        value  =        1 * 10**10 + \
                number[0] * 10**8  + \
                number[1] * 10**6  + \
                number[2] * 10**4  + \
                number[3] * 10**2  + \
                number[4] * 10**0 
        return(value)

    def value_pair(self):
        single_list = []
        pair_list   = []
        
        for i in set(self.numbers):
            if( self.numbers.count(i) ) == 1: single_list = single_list + [i]
            if( self.numbers.count(i) ) == 2: pair_list   = pair_list   + [i]
                
        single_number = sorted( [self.number_mapping[n] for n in single_list],  reverse=True)
        pair_number   = sorted( [self.number_mapping[n] for n in   pair_list],  reverse=True)
    
        value =                 2 * 10**10 + \
                   pair_number[0] * 10**8  + \
                 single_number[0] * 10**6  + \
                 single_number[1] * 10**4  + \
                 single_number[2] * 10**2  + \
                                0 * 10**0 
        return(value)

    def value_two_pairs(self):    
        single_list = []
        pair_list   = []
        
        for i in set(self.numbers):
            if( self.numbers.count(i) ) == 1: single_list = single_list + [i]
            if( self.numbers.count(i) ) == 2: pair_list   = pair_list + [i]
                
        single_number = sorted( [self.number_mapping[n] for n in single_list],  reverse=True)
        pair_number   = sorted( [self.number_mapping[n] for n in   pair_list],  reverse=True)
        
        value =                 3 * 10**10 + \
                   pair_number[0] * 10**8  + \
                   pair_number[1] * 10**6  + \
                 single_number[0] * 10**4  + \
                                0 * 10**2  + \
                                0 * 10**0 
        return(value)  

    def value_three_of_a_kind(self):
        single_list = []
        triple_list = []
        
        for i in set(self.numbers):
            if( self.numbers.count(i) ) == 1: single_list = single_list + [i]
            if( self.numbers.count(i) ) == 3: triple_list = triple_list + [i]
                
        single_number = sorted( [self.number_mapping[n] for n in single_list],  reverse=True)
        triple_number = sorted( [self.number_mapping[n] for n in triple_list],  reverse=True)
        
        value =                 4 * 10**10 + \
                 triple_number[0] * 10**8  + \
                 single_number[0] * 10**6  + \
                 single_number[1] * 10**4  + \
                                0 * 10**2  + \
                                0 * 10**0 
        return(value)  
        
    def value_straight(self):
        number = sorted( [self.number_mapping[n] for n in self.numbers],  reverse=True)
    
        # handle the case of 12345
        if( number[0] == 14 and number[-1] == 2):
            number[0] = 1
        
        value  =        5 * 10**10 + \
                number[0] * 10**8  + \
                        0 * 10**6  + \
                        0 * 10**4  + \
                        0 * 10**2  + \
                        0 * 10**0 
        
        return(value)

    def value_flush(self):  
        number = sorted( [self.number_mapping[n] for n in self.numbers],  reverse=True)
        
        value  =        6 * 10**10 + \
                number[0] * 10**8  + \
                number[1] * 10**6  + \
                number[2] * 10**4  + \
                number[3] * 10**2  + \
                number[4] * 10**0 
        return(value)

    def value_full_house(self):
        pair_list   = []
        triple_list = []
        
        for i in set(self.numbers):
            if( self.numbers.count(i) ) == 2: pair_list   = pair_list   + [i]
            if( self.numbers.count(i) ) == 3: triple_list = triple_list + [i]
                
        pair_number   = sorted( [self.number_mapping[n] for n in pair_list  ], reverse=True)
        triple_number = sorted( [self.number_mapping[n] for n in triple_list], reverse=True)
        
        value =                 7 * 10**10 + \
                 triple_number[0] * 10**8  + \
                   pair_number[0] * 10**6  + \
                                0 * 10**4  + \
                                0 * 10**2  + \
                                0 * 10**0 
        return(value)
        
    def value_full_of_a_kind(self):
        single_list    = []
        quadruple_list = []
        
        for i in set(self.numbers):
            if( self.numbers.count(i) ) == 1: single_list    =    single_list + [i]
            if( self.numbers.count(i) ) == 4: quadruple_list = quadruple_list + [i]
                
        single_number    = sorted( [self.number_mapping[n] for n in single_list   ], reverse=True)
        quadruple_number = sorted( [self.number_mapping[n] for n in quadruple_list], reverse=True)
        
        value =                 8 * 10**10 + \
              quadruple_number[0] * 10**8  + \
                 single_number[0] * 10**6  + \
                                0 * 10**4  + \
                                0 * 10**2  + \
                                0 * 10**0 
        return(value)   
        
    def value_straight_flush(self):
        number = sorted( [self.number_mapping[n] for n in self.numbers],  reverse=True)
    
        # handle the case of 12345
        if( number[0] == 14 and number[-1] == 2):
            number[0] = 1
        
        value  =        9 * 10**10 + \
                number[0] * 10**8  + \
                        0 * 10**6  + \
                        0 * 10**4  + \
                        0 * 10**2  + \
                        0 * 10**0 
        
        return(value)

if __name__ == '__main__':
    print( Hand( ["10c", "4h", "7d", "Kc", "2s"]  ).value) # high_card 
    print( Hand( ["Kc",  "Kh", "7d", "2c", "5s"]  ).value) # pair
    print( Hand( ["Kc",  "Kh", "7d", "7c", "5s"]  ).value) # two_pair
    print( Hand( ["Kc",  "Kh", "Kd", "7c", "5s"]  ).value) # three_of_a_kind
    print( Hand( ["3c",  "4h", "5d", "6c", "7s"]  ).value) # straight
    print( Hand( ["3c",  "4c", "5c", "6c", "8c"]  ).value) # flush
    print( Hand( ["Kc",  "Kh", "Kd", "7c", "7s"]  ).value) # full_house
    print( Hand( ["6c",  "6h", "6d", "6s", "Ks"]  ).value) # full_of_a_kind
    print( Hand( ["10s",  "Js", "Qs", "Ks", "1s"] ).value) # straight_flush