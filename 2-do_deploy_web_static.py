#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo
Deploys the archive to web servers
"""
from fabric.api import local, put, env, run, sudo
import datetime
from fabric.decorators import runs_once

env.hosts = ["100.26.216.42", "54.84.238.169"]
env.users = ["ubuntu"]


@runs_once
def do_pack():
    """
    Creates a timestamped .tgz archive
    of the files in the web_static folder.
    """

    local("mkdir -p versions")

    now = datetime.datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    directory = "web_static"
    path = "versions/{}".format(archive_name)

    result = local("tar -czvf {} {}".format(
             path, directory), capture=True)

    if result.failed:
        return None
    else:
        return path


def do_deploy(archive_path):
    """
    distributes an archive to web servers
    False if the file at the path archive_path doesn’t exist
    """
    if not local("test -e {}".format(archive_path)).succeeded:
        return False

    try:
        put(archive_path, '/tmp/')
        # Uncompress the archive
        archive_filename = archive_path.split('/')[-1]
        folder_name = archive_filename.replace(
                      '.tgz', '').replace('.tar.gz', '')
        run("mkdir -p /data/web_static/releases/{}".format(folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, folder_name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Delete the symbolic link /data/web_static/current from the web server
        sudo("rm /data/web_static/current", warn_only=True)

        # Create a new symbolic link, linked to the new version
        sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current"
             .format(folder_name))

        return True
    except Exception as e:
        print("Exception:", e)
        return False
