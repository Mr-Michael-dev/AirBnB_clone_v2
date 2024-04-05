#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo
"""
import fabric
import datetime
import os


def do_pack():
    """
    Creates a timestamped .tgz archive
    of the files in the web_static folder.
    """

    now = datetime.datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    directory = "web_static"
    arc_path = "./versions/{}".format(archive_name)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    arc_path = os.path.join("versions", archive_name)

    result = fabric.operations.local("tar -czvf {} {}".format(
             arc_path, directory), capture=True)

    if result.failed:
        return None
    else:
        return arc_path
