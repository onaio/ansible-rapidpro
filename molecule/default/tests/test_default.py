import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rapidpro_service(host):
    rapidpro = host.service("rapidpro")
    assert rapidpro.is_running
    assert rapidpro.is_enabled

    celeryD = host.service("celeryd-rapidpro")
    assert celeryD.is_running
    assert celeryD.is_enabled

    celeryBeat = host.service("celerybeat-rapidpro")
    assert celeryBeat.is_running
    assert celeryBeat.is_enabled


def test_rapidpro_app_files(host):
    appDir = host.file("/home/rapidpro/app")
    assert appDir.exists
    assert appDir.user == "rapidpro"
    assert appDir.group == "rapidpro"
    assert appDir.is_symlink
    assert appDir.linked_to == "/home/rapidpro/app-versioned/v5.0.9"

    appVersionedDir = host.file("/home/rapidpro/app-versioned/v5.0.9")
    assert appVersionedDir.exists
    assert appVersionedDir.user == "rapidpro"
    assert appVersionedDir.group == "rapidpro"
    assert appVersionedDir.is_directory
    assert oct(appVersionedDir.mode) == "0o755"

    mediaDir = host.file("/home/rapidpro/media")
    assert mediaDir.exists
    assert mediaDir.user == "rapidpro"
    assert mediaDir.group == "rapidpro"
    assert mediaDir.is_directory
    assert oct(mediaDir.mode) == "0o775"

    virtualenv = host.file("/home/rapidpro/.virtualenvs/rapidpro")
    assert virtualenv.exists
    assert virtualenv.user == "rapidpro"
    assert virtualenv.group == "rapidpro"
    assert virtualenv.is_directory
    assert oct(virtualenv.mode) == "0o755"
