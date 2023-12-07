#!/usr/bin/python3
"""Fabric script that generates a .tzg archive"""


def do_pack():
    """Pack the web_static file"""
    from fabric.api import local
    from datetime import datetime
    import os

    archive = "versions/web_static_{}.tgz".format(datetime.now().strftime(
        "%Y%m%d%H%M%S"))
    os.makedirs("versions",  exist_ok=True)
    result = local("tar -cvzf {} web_static".format(archive))

    return result if result.succeeded else None
