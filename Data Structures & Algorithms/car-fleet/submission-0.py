class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)

        times =[] 

        for position,speed in cars:
            time = (target - position) / speed

            if not times:
                times.append(time)

            elif time > times[-1]:
                times.append(time)
            
        return len(times)
        

        
        




            
            

        