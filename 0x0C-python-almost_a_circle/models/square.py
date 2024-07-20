#!/usr/bin/python3
"""This model defines the square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the constructor class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method returns the informal representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}"
