from django import template
from django.conf import settings
import subprocess
import os

register = template.Library()

try:
    #cmd = "cd " + settings.GIT_ROOT + "; git log --pretty=format:\"%h %ai\" --abbrev-commit --date=short -1"
    # cmd =  "cd " + settings.GIT_ROOT + "; git describe"
    # head = subprocess.Popen(cmd,
    #                         shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # GIT_SHORT = "<b>" + head.stdout.readline().strip() + "</b>"

    cmd =  "cd " + settings.GIT_ROOT + "; git log --pretty=format:' %h - %cd' --abbrev-commit --date=short -1"
    head = subprocess.Popen(cmd,
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    GIT_SHORT = head.stdout.readline().strip().decode('utf-8')

except Exception as e:
    print(e)
    GIT_SHORT = u'unknown'


@register.simple_tag
def git_short_version():
    return os.environ.get('GIT_SHORT_VERSION', GIT_SHORT)
