import http.server
import socketserver
import re

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            with open('szablon.html', 'r', encoding='utf-8') as template_file:
                template_content = template_file.read()

            with open('article.html', 'r', encoding='utf-8') as article_file:
                article_content = article_file.read()

            # Use regular expression to replace the content inside the <body> tag
            body_pattern = re.compile(r'(<body.*?>)(.*?)(</body>)', re.DOTALL)
            filled_template = body_pattern.sub(r'\1' + article_content + r'\3', template_content)

            self.wfile.write(filled_template.encode('utf-8'))

        else:
            self.send_error(404)

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()