import BaseHTTPServer
import SimpleHTTPServer


SimpleHTTPServer.SimpleHTTPRequestHandler.
httpd = BaseHTTPServer.HTTPServer(('localhost', 4000), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.serve_forever()
