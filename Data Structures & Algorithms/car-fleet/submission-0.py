class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed))
        position, speed = map(list, zip(*sorted_pairs))
        stack = []

        for i in range(len(position)-1, -1, -1):
            if stack:
                fc_i = stack[-1]
                fc_time = (target - position[fc_i])/speed[fc_i]
                bc_time = (target - position[i])/speed[i]

                if bc_time>fc_time:
                    stack.append(i)
            else:
                stack.append(i)
            
        
        return len(stack)