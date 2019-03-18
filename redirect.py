from http.server import BaseHTTPRequestHandler

urls = {
  'indyrb': '/notes/meetups',
  'default': 'https://nic.oll.is'
}

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        shortcode = self.path[1:]

        if shortcode in urls:
            url = urls[shortcode]
        else :
            url = urls['default']

        self.send_response(302)
        self.send_header('Location', url)
        self.end_headers()
        return
