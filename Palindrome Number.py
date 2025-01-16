def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """


        #Given an integer x, return true if x is a palindrome, and false otherwise.
        string_invertida = ""
        string_numero = str(x)
        for i in range(len(string_numero)):
            idx = len(string_numero)-i                       
            string_invertida += string_numero[idx-1]
        
        if(string_invertida==string_numero):
            return True
        else:
            return False




print(isPalindrome(000))
                
                

                

              


            
        