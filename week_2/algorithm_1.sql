BEGIN SwapAges
    DISPLAY "Enter first name:"
    GET name1
    DISPLAY "Enter age for " + name1
    GET age1
    
    DISPLAY "Enter second name:"
    GET name2
    DISPLAY "Enter age for " + name2
    GET age2
    
    DISPLAY "Before swap:"
    DISPLAY name1 + " is " + age1 + " years old"
    DISPLAY name2 + " is " + age2 + " years old"
    
    SET temp = age1
    SET age1 = age2
    SET age2 = temp
    
    DISPLAY "After swap:"
    DISPLAY name1 + " is now " + age1 + " years old"
    DISPLAY name2 + " is now " + age2 + " years old"
END SwapAges