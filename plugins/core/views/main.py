import logging
import subprocess

import ajenti
from ajenti.api import *
from ajenti.api.http import BaseHttpHandler, url, HttpPlugin, SocketEndpoint
from ajenti.plugins import PluginManager

from ajenti.plugins.core.api.endpoint import endpoint


@component(HttpPlugin)
class Handler (HttpPlugin):
    def __init__(self, context):
        pass

    @url('/')
    @endpoint(page=True, auth=False)
    def handle_root(self, http_context):
        return http_context.redirect('/view/')


    @url('/view/.*')
    @endpoint(page=True, auth=False)
    def handle_view(self, http_context):
        if ajenti.dev:
            cmd = ['./scripts/build-resources']
            if http_context.env.get('HTTP_CACHE_CONTROL', None) == 'no-cache':
                cmd += ['nocache']
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o, e = p.communicate()
            if p.returncode != 0:
                logging.error('Resource compilation failed')
                logging.error(o + e)
            
        path = PluginManager.get(ajenti.context).get_content_path('core', 'content/pages/index.html')
        content = open(path).read() % {
            'prefix': http_context.prefix,
        }
        http_context.add_header('Content-Type', 'text/html')
        http_context.respond_ok()
        return content
