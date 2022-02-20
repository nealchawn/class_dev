import math
def poly_area(n,s):
    """
        The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    """
    if n <= 0 or s <= 0:
        return 0
    return((1/4)*n*s**2)/math.tan(math.pi/n)

def poly_perimeter(n, s):
    """
        The perimeter of a polygon is: length of the boundary of the polygon
    """
    return n*s

def polysum(n, s):
    """
        Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. 
        This function should sum the area and square of the perimeter of the regular polygon. 
        The function returns the sum, rounded to 4 decimal places.
    """
    return round((poly_area(n,s) + poly_perimeter(n,s)**2),4)