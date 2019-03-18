from http.server import BaseHTTPRequestHandler

urls = {
  'indyrb': 'https://gist.github.com/nicollis/972ae12c823b853a01b5f57ef961f4f7',
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
