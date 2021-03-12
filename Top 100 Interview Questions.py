# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        
        output = []
        
        if len(nums1) <= len(nums2):
            output = self.remove(nums1, nums2)
        
        else:
            output = self.remove(nums2, nums1)
        
        return output

            
    
    def remove(self, li_short:List[int], li_long:List[int]) -> List[int]:
        output = []
        for element in li_short:
                try:
                    li_long.remove(element)
                    output.append(element)
                except ValueError:
                    continue
        return output
            
                    