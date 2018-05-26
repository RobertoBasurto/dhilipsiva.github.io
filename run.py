from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('dhilipsiva.github.io', 'source'),
    autoescape=select_autoescape(['html'])
)
template = env.get_template('mytemplate.html')
__import__('ipdb').set_trace()

'''
import os
import sys
import time
import logging
import http.server
import socketserver

import sass
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()




os.mkdir('css')
os.mkdir('sass')
scss = """\
$theme_color: #cc0000;
body {
    background-color: $theme_color;
}
"""
with open('sass/example.scss', 'w') as example_scss:
     example_scss.write(scss)

sass.compile(dirname=('sass', 'css'), output_style='compressed')
with open('css/example.css') as example_css:
    print(example_css.read())
'''
