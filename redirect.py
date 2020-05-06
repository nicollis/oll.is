from http.server import BaseHTTPRequestHandler

urls = {
  'indyrb': '/notes/meetups',
  'deconstruct-cfp': 'https://drive.google.com/uc?id=1-vifClWz4WA9ceJeBVmFLM994qfmelCg&export=download',
  'leanor': 'https://www.icloud.com/sharedalbum/#B0mJtdOXmtwgmEY',
  'newsletter' : 'https://tinyletter.com/ML-Roundup',
  'newsletter-submission': 'https://docs.google.com/forms/d/e/1FAIpQLSfCbsca4KkDcUb5AA2ko7aX5xWHYbmOg8QpJaNZQsUTUVLz6A/viewform?usp=sf_link',
  'meeting': 'https://zoom.us/j/8912004048?pwd=SUZGL0pUS01wa3d4WmhCZlNEY0x6QT09',
  'meet': 'https://zoom.us/j/8912004048?pwd=SUZGL0pUS01wa3d4WmhCZlNEY0x6QT09',
  'datacamp': 'https://www.datacamp.com?tap_a=5644-dce66f&tap_s=889499-d58a3b&utm_medium=affiliate&utm_source=nicholasollis',
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
