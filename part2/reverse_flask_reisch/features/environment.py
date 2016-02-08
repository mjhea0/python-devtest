import os
import sys

pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
base_path = pwd.strip(project)
new_path = os.path.join(base_path, 'project')

try:
    from project import app
except ImportError:
    sys.path.append(full_path)
    from project import app


def before_feature(context, feature):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    context.client = app.test_client()
