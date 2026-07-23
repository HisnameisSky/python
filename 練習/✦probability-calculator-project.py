import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            all_balls = self.contents[:]
            self.contents.clear()
            return all_balls
        
        drawn_balls = []
        for _ in range(num_balls):
            random_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(random_index))
            
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
            
        success = True
        for color, expected_count in expected_balls.items():
            if drawn_counts.get(color, 0) < expected_count:
                success = False
                break
                
        if success:
            success_count += 1
            
    return success_count / num_experiments