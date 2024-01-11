#!/usr/bin/python3
"""Fabric script that distributes an archive to the web servers
The do_deploy() function takes in an archive path and deploys it to the web servers by:
1. Checking if the archive path exists, returning False if it doesn't 
2. Extracting the archive name and removing the extension
3. Uploading the archive to /tmp/ on the servers
4. Creating a releases directory with the archive name 
5. Extracting the archive to the releases directory
6. Removing the uploaded archive from /tmp/
7. Moving the web_static content into the release directory
8. Removing the now empty web_static directory
9. Deleting any existing /data/web_static/current symlink 
10. Creating a symlink from /data/web_static/current to the new release
11. Returning True if successful, False otherwise
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.27.13.221', '54.210.79.93']


def do_deploy(archive_path):
    """deploy the archive to the web servers
    Args:
        archive_path (Any): _description_
    Returns:
        boolean: _description_
    """
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
