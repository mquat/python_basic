from typing import List

def trapping_rain(height_list: List[str])-> int:
    stack  = []
    volume = 0

    for i in range(len(height_list)):
        while stack and height_list[i] > height_list[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break
        
            distance = i - stack[-1] - 1
            water = min(height_list[i], height_list[stack[-1]]) - height_list[top]

            volume += distance * water

        stack.append(i)

    return volume


height_list = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rain(height_list))