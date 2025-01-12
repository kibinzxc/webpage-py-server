import sys
import http.server
import socketserver

# Create a request handler
HandlerClass = http.server.SimpleHTTPRequestHandler

# Create the HTTP server class
ServerClass = http.server.HTTPServer

# Define protocol
Protocol = "HTTP/1.0"

# Get port number from command line or use default
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000  # Default port

# Set up the server address (use your machine's IP address here)
server_address = ('192.168.1.72', port)  # Replace with your actual IP for network access

# Configure the handler protocol
HandlerClass.protocol_version = Protocol

# Create the server
http = ServerClass(server_address, HandlerClass)

# Log server details
sa = http.socket.getsockname()
print(f"Serving HTTP on {sa[0]} port {sa[1]}...")

# Start the server
http.serve_forever()
