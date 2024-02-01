#!/usr/bin/python3
"""
 Fabric script that distributes an archive to your web servers
"""

from fabric.api import *
from fabric.contrib import files
import os

env.hosts = ['35.153.66.132', '54.89.25.180']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """The function to transfer archive_path to web_server"""

    if not os.path.isfile(archive_path):
        return False

    with cd('/tmp'):
        # Extract informatin from the archive_path
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            # Upload the archive to the web server's /tmp dir
            putpath = put(archive_path)

            # If the release dirctory exists, remove it
            if files.exists(outpath):
                run('rm -rdf {}'.format(outpath))

            # Crerate the release dir target
            run('mkdir -p {}'.format(outpath))

            # Unpack the content of the archive to the release dirctory
            run('tar -xzf {} -C {}'.format(putpath[0], outpath))

            # Remove the uploaded archive
            run('rm -f {}'.format(putpath[0]))

            # Move web_static directory to the release dir
            run('mv -u {}/web_static/* {}'.format(outpath, outpath))

            # Remove the original web_static in release dir
            run('rm -rf {}/web_static'.format(outpath))

            # Remove the existing symbol link
            run('rm -rf /data/web_static/current')

            # Create a new symbolic_link
            run('ln -sf {} /data/web_static/current'.format(outpath))

            print('A new version deployed!')

            run('sudo systemctl restart nginx')
        except Exception as e:
            print(e)
            return False
        else:
            return True
