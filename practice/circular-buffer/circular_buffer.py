"""
Approach:
1. Define two custom exception classes, BufferFullException and BufferEmptyException, inherited from BufferError.
   These exceptions are raised when the circular buffer is full or empty, respectively.
2. Implement the CircularBuffer class to simulate a circular buffer data structure.
3. Initialize the CircularBuffer with a given capacity and an empty store to hold the data.
4. Implement methods for reading, writing, overwriting, and clearing the buffer:
    - read(): Reads data from the buffer. Raises BufferEmptyException if the buffer is empty.
    - write(data): Writes data to the buffer. Raises BufferFullException if the buffer is full.
    - overwrite(data): Overwrites data in the buffer. If the buffer is full, replaces the oldest data.
    - clear(): Clears the buffer by resetting the store to an empty list.
5. Each method includes error handling to raise the appropriate exception if the buffer is full or empty.
"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        # Initialize BufferFullException with an error message
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        # Initialize BufferEmptyException with an error message
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        # Initialize CircularBuffer with capacity and an empty store
        self.capacity = capacity
        self.store = []

    def read(self):
        # Read data from the buffer
        if len(self.store) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        out = self.store[0]
        self.store.remove(out)
        return out   
        
    def write(self, data):
        # Write data to the buffer
        if len(self.store) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.store.append(data)

    def overwrite(self, data):
        # Overwrite data in the buffer
        if len(self.store) == self.capacity:
            self.store = self.store[1:] + [data]
        else:
            self.store.append(data)

    def clear(self):
        # Clear the buffer
        self.store = []
