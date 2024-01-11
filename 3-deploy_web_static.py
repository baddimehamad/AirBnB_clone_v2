#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder, 
deploy it to web servers, and unpack/install it in the /data/web_static/ 
folder on the servers.

do_pack() creates the .tgz archive locally.
do_deploy() uploads and installs the archive on the servers.
deploy() calls do_pack() and do_deploy().

env.hosts contains the host server addresses.
"""

from fabric.api import env, local, put, run

from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.27.13.221', '54.210.79.93']


def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
