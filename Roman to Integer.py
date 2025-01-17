
def romanToInt( s):
        """
        :type s: str
        :rtype: int
        """
        numeros_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        total = 0
        for index, roman_number in enumerate(s):
            
            if(index + 1 == len(s)):
                if(numeros_romanos[roman_number] <= numeros_romanos[s[index-1]]):
                    total += numeros_romanos[roman_number]
                    return total
                else:
                    return total
            if(index + 1 < len(s) ):
                if(numeros_romanos[roman_number] >=  numeros_romanos[s[index+1]]):
                    controle = 0 
                    if(index >0):
                         if(numeros_romanos[roman_number] > numeros_romanos[s[index-1]]):
                            controle  = 1                                   
                    if(controle == 0):     
                        total +=  numeros_romanos[roman_number]
                else:
                    total +=  numeros_romanos[s[index+1]] - numeros_romanos[roman_number]
                 
        
                                                               
            
print(romanToInt("MCMXCIV"))   