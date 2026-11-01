class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        basket = {}
        left=0
        max_fruits = 0
        for right in range(len(fruits)):
            right_fruits = fruits[right]
            basket[right_fruits] = basket.get(right_fruits,0)+1

            while len(basket) > 2:
                left_fruits = fruits[left]
                basket[left_fruits]-=1

                if (basket[left_fruits]==0):
                    del basket[left_fruits]
                left+=1
            max_fruits = max(max_fruits, right-left+1)
        return max_fruits        

            