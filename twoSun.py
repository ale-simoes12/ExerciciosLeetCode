
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lista_idx = []
        dicionario_par = {}
        for index, numero in enumerate(nums):
            if numero in dicionario_par:
                lista_idx.append(dicionario_par[numero])
                lista_idx.append(index)
                return lista_idx
            else:      
                dicionario_par[target - numero] =  index

            
                


            

