def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # prefix = {}
        # for idx  , c in enumerate(str(0)):
        #     prefix[idx] = c         

        # contador = 1
        # controle = 0
        prefixo = strs[0]
        del strs[0]
        if( len(strs) < 1):
            return prefixo
        if(len(prefixo) < 1):
            return ""
        if(strs[0] == "" ):
            return ""

        if(prefixo[0] != strs[0][0]):
            return ""
        for idx , string in enumerate(strs):
            if(string == ""):
                return ""

            tamanho_pre = len(prefixo)
            continuar = False
            
            while (tamanho_pre) > 0 and continuar == False:        
                if prefixo in string:
                    for idx , c in enumerate(prefixo):
                        if(c == string[idx]):
                            continue    
                        else:
                            prefixo = prefixo[:-1]
                            tamanho_pre -=1       
                    continuar  = True
                       
                else:    
                    prefixo = prefixo[:-1]
                    tamanho_pre -=1
            if (tamanho_pre)  == 0:
                 return ""       

        return prefixo

        

entrada = ["flower","flow","flight"]
print(longestCommonPrefix(entrada))                 
                 
        