"""
Approach:
- The code defines two classes, MeteredFile and MeteredSocket, to measure the I/O operations performed on files and sockets.
- MeteredFile subclass extends BufferedRandom for file I/O operations.
- MeteredSocket encapsulates socket operations.
- Each class tracks read and write operations along with the number of bytes read and written.
- Renamed variables to adhere to Python naming conventions (snake_case) and improve readability.
"""
import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_ops = 0
        self._write_ops = 0
        self._read_bytes = 0
        self._write_bytes = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        line = super().readline()
        self._read_ops += 1
        self._read_bytes += len(line)
        if line:
            return line
        raise StopIteration()
    
    def read(self, size=-1):
        buf = super().read(size)
        self._read_ops += 1
        self._read_bytes += len(buf)
        return buf
    
    @property
    def read_bytes(self):
        return self._read_bytes
    
    @property
    def read_ops(self):
        return self._read_ops
    
    def write(self, b):
        bytes_written = super().write(b)
        self._write_ops += 1
        self._write_bytes += bytes_written
        return bytes_written
    
    @property
    def write_bytes(self):
        return self._write_bytes
    
    @property
    def write_ops(self):
        return self._write_ops

class MeteredSocket:
    """Implement using a delegation model."""
    
    def __init__(self, socket):
        self._recv_ops = 0
        self._send_ops = 0
        self._recv_bytes = 0
        self._send_bytes = 0
        self._socket = socket
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)
    
    def recv(self, bufsize, flags=0):
        self._recv_ops += 1
        received_data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(received_data)
        return received_data
    
    @property
    def recv_bytes(self):
        return self._recv_bytes
    
    @property
    def recv_ops(self):
        return self._recv_ops
    
    def send(self, data, flags=0):
        self._send_ops += 1
        bytes_sent = self._socket.send(data, flags)
        self._send_bytes += bytes_sent
        return bytes_sent
    
    @property
    def send_bytes(self):
        return self._send_bytes
    
    @property
    def send_ops(self):
        return self._send_ops
