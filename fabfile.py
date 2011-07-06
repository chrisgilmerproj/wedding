"""
fab deployment script
====================================

"""
import os

from fabric.api import *
from fabric.contrib.project import *

from fab_deploy import *

def my_site():
    """ Default Configuration """
    env.conf = dict(
        PROVIDER = '', # 'ec2_us_east','ec2_us_west'
		AWS_ACCESS_KEY_ID = '',
		AWS_SECRET_ACCESS_KEY = '',

		CONF_FILE = os.path.join(os.getcwd(),'fabric.conf'),
        INSTANCE_NAME = 'project_name',
        REPO = 'http://some.repo.com/project_name/',
    )

my_site()

