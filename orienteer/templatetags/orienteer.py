#!/usr/bin/python2.5
#
# Copyright 2010 Sentinel Design. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Simple Compass integration for Django'''

__author__ = 'Drew Yeaton <drew@sentineldesign.net>'
__version__ = '0.2'


import os
from commands import getstatusoutput

from django import template
from django.conf import settings


register = template.Library()

@register.simple_tag
def compass(filename, media):
    import time
    
    proj_dir = settings.COMPASS_PROJECT_DIR
    output_dir = settings.COMPASS_OUTPUT_DIR
    output_url = settings.COMPASS_OUTPUT_URL
    
    needs_update = False

    # get timestamp of css, if it doesn't exist we need to make it
    try:
        stat = os.stat(proj_dir + filename + '.css')
        output_file_ts = stat.st_mtime
    except:
        output_file_ts = '1'
    
    css = "<link rel='stylesheet' href='%s?%s' type='text/css' media='%s' />" % (output_url + filename + '.css', output_file_ts, media)
    
    # if we aren't debugging (in production for example), short-cicuit this madness
    if not settings.TEMPLATE_DEBUG:
        return css
    
    cmd_dict = {
        'bin': settings.COMPASS_BIN, 
        'sass_style': settings.COMPASS_STYLE, 
        'project_dir': proj_dir,  
        'output_dir': output_dir, 
    }
    
    cmd = "%(bin)s compile -s %(sass_style)s --css-dir %(output_dir)s %(project_dir)s" % cmd_dict
    (status, output) = getstatusoutput(cmd)
    print output
    
    return css
