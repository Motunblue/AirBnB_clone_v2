#!/usr/bin/python3
"""Deploy web static page"""
from fabric.api import put, env, run

env.hosts = ['18.234.107.108', '18.207.235.223']


def do_deploy(archive_path):
    """Deploy archived web static page"""
    if not archive_path:
        return False

    file_name = archive_path[archive_path.find('w'):archive_path.find('.')]
    r = put(archive_path, "/tmp/{}.tgz".format(file_name))
    if r.failed:
        return False
    r = run("mkdir -p /data/web_static/releases/{}/".format(file_name))
    if r.failed:
        return False
    r = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
        file_name, file_name))
    if r.failed:
        return False
    r = run("rm /tmp/{}.tgz".format(file_name))
    if r.failed:
        return False
    r = run(f"mv /data/web_static/releases/{file_name}/web_static/* \
        /data/web_static/releases/{file_name}/")
    if r.failed:
        return False
    r = run(f"rm -rf /data/web_static/releases/{file_name}/web_static")
    if r.failed:
        return False
    r = run("rm -rf /data/web_static/current")
    if r.failed:
        return False
    r = run(f"ln -s /data/web_static/releases/{file_name}/ \
        /data/web_static/current")
    if r.failed:
        return False
    return True
