# python -m http.server 8080
import os
import http.server
import socketserver
import webbrowser
# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/
# http://www.powenko.com/wordpress/%E5%BB%BA%E7%AB%8B%E4%B8%80%E5%80%8B-web-server-%E5%92%8C-%E8%A6%96%E7%AA%97%E7%9A%84python-%E7%A8%8B%E5%BC%8F/
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class MyHttpRequestHandler(http.server.CGIHTTPRequestHandler):
    http.server.CGIHTTPRequestHandler.cgi_directories = ["/"] 
    def do_GET(self):
        # if self.path == '/':
        #     self.path = 'CodeMirror/codemirror-5.49.2/sublime_editor.html'
        # return http.server.SimpleHTTPRequestHandler.do_GET(self)
        if os.access('.' + os.sep + self.path, os.R_OK):
            http.server.CGIHTTPRequestHandler.do_GET(self);
        else:
            # print("--------------------------3")
            # self.send_response(200)
            # self.send_header('Content-Type', 'text/html')
            # # self.send_header('Location', '%s%s%s'%('http://localhost:', PORT, self.path))
            # self.end_headers()
            # self.wfile.write(bytes((open(os.path.join('CodeMirror/codemirror-5.49.2', "sublime_editor.html")).read()), "utf8"))
            # print("--------------------------4")
            self.send_error(404,'Not Found: %s' % self.path)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8080
# my_server = socketserver.TCPServer(("", PORT), handler_object)
my_server = http.server.HTTPServer(("", PORT), handler_object)

url = '%s%s%s'%('http://127.0.0.1:', PORT, '/CodeMirror/codemirror-5.49.2/sublime_editor.html')
webbrowser.open(url, new=2)

# Star the server
my_server.serve_forever()
