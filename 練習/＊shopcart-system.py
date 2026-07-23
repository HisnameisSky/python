import math

class OrderBox:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def height(self,height):
        self.height=height
    
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return math.sqrt((self.width**2)+(self.height**2))
    def get_picture(self):
        if self.width>50 or self.height>50:
            return "Too big for picture."
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self,small_box):
        horizontal_fit=self.width//small_box.width
        vertical_fit=self.height//small_box.height
        return horizontal_fit*vertical_fit
    
    def __str__(self):
        return f"OrderBox(width={self.width}, height={self.height})"
    
class GiftSet(OrderBox):
        def __init__(self,side):
            super().__init__(side,side)
        def set_side(self,side):
            self.width=side
            self.height=side
        def set_width(self,width):
            self.set_side(width)
        def height(self,height):
            self.set_side(height)
        
        def __str__(self):
            return f"GiftSet(side={self.width})"

big_box=OrderBox(101,52)
print(big_box.get_area())
print(big_box)

small_gift=GiftSet(301)
print(small_gift.get_area())
print(small_gift)

small_gift.set_width(41)
print(small_gift)

print(big_box.get_amount_inside(small_gift))

##
