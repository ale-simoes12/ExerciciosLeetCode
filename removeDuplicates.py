def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numeros = []
        k = 0 
        for numero in nums:
            if numero in numeros:
                continue
            else:
                k+=1
                numeros.append(numero)


        return numeros, k

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
                    


                            
        