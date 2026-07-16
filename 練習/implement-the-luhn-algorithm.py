def verify_card_number(card_number_str: str) -> str:
    
    cleaned_number = card_number_str.replace('-', '').replace(' ', '')
    
    digits = [int(char) for char in cleaned_number]
    
    
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
        
    
    total_sum = sum(digits)
    
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"



if __name__ == '__main__':
    print(verify_card_number('453914889'))             
    print(verify_card_number('4111-1111-1111-1111'))
    print(verify_card_number('453914881')) 
    print(verify_card_number('1234 5678 9012 3456'))