class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        fleet = []

        for position,speed in cars:
            time = (target - position) / speed
            
            if not fleet:
                fleet.append(time)

            elif time > fleet[-1]:
                fleet.append(time)

            
        return len(fleet)
        
        

        
        




            
            

        