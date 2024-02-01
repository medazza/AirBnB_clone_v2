#!/usr/bin/python3
"""Create and distributes an archive to web servers  """

from fabric.api import *
from fabric.operations import run, put, sudo
from datetime import date
import os.path
import time

env.hosts = ['35.153.66.132', '54.89.25.180']


def do_pack():
    """func and store the path of the created archive"""
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(
            timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def do_deploy(archive_path):
    """ function using the new path of the new archive"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        # upload the archive to /tmp/ dir
        put(archive_path, "/tmp/")
        archive_name = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + archive_name.split(".")[0])
        run("sudo mkdir -p {:s}".format(folder))

        # Uncompress the archive to the folder /data/web...
        run("sudo tar -xzf /tmp/{:s} -C {:s}".format(archive_name, folder))

        # Delete the archive from the web server
        run("sudo rm /tmp/{:s}".format(archive_name))
        run("sudo mv {:s}/web_static/* {:s}/".format(folder, folder))
        run("sudo rm -rf {:s}/web_static".format(folder))

        # Delet the symbolic link /data/web_static...
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('sudo ln -s {:s} /data/web_static/current'.format(folder))
        print('New version deployed!')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def deploy():
    """Create and distributes archive to web servers"""
    try:
        archive_path = do_pack()
        deploythis = do_deploy(archive_path)
        return deploythis
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
