"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0) 
        """Makes a new serial generator, starts at set start point"""
        self.start = self.next = start

    def __repr__(self)
        """gives representation of generator"""
        return f"<Serial generator start={self.start} next={self.next}>"

    def generate(self)
        """Returns next serial number"""
        self.next += 1
        return self.next - 1   
        
    def reset(self)
        """Sets number back to start"""
        self.next = self.start