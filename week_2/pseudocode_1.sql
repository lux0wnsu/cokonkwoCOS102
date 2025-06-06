BEGIN StoreCheckout
    DISPLAY "Scan items"
    SET total = 0
    
    WHILE more items to scan DO
        GET item price
        ADD item price to total
    END WHILE
    
    DISPLAY "Subtotal: " + total
    CALCULATE tax = total * tax_rate
    DISPLAY "Tax: " + tax
    CALCULATE final_total = total + tax
    DISPLAY "Total: " + final_total
    
    DISPLAY "Select payment method"
    GET payment_method
    
    IF payment_method is credit/debit THEN
        PROCESS card payment
        PRINT receipt
    ELSE IF payment_method is cash THEN
        GET amount_tendered
        CALCULATE change = amount_tendered - final_total
        DISPLAY "Change due: " + change
        GIVE change to customer
        PRINT receipt
    END IF
    
    DISPLAY "Thank you for your purchase!"
END StoreCheckout