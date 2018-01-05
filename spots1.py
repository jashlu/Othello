import point1



class Spot:
    def __init__(self, center: point1.Point, radius_frac: float):
        self._center = center
        self._radius_frac = radius_frac


    def center(self) -> point1.Point:
        return self._center


    def radius_frac(self) -> float:
        return self._radius_frac


    def contains(self, point: point1.Point) -> bool:
        return self._center.frac_distance_from(point) <= self._radius_frac
    


class SpotsState:
    def __init__(self):
        self.black_spots = []
        self.white_spots = []


    def all_black_spots(self) -> [Spot]:
        return self.black_spots
    
    def all_white_spots(self) -> [Spot]:
        return self.white_spots


    def handle_black_click(self, click_point: point1.Point) -> None:
        for spot in reversed(self.black_spots):
            if spot.contains(click_point):
                self.black_spots.remove(spot)
                return
            
        self.black_spots.append(Spot(click_point, 0.05))
        
    def handle_white_click(self, click_point: point1.Point)-> None:
        for spot in reversed(self.white_spots):
            if spot.contains(click_point):
                self.white_spots.remove(spot)
                return
            
        self.white_spots.append(Spot(click_point, 0.05))


        

