"""Old maintenance script from the PHP days. Nothing imports or schedules it anymore."""
import subprocess
import sys


def purge_tenant(tenant):
    subprocess.call("rm -rf /var/data/tenants/" + tenant, shell=True)


if __name__ == "__main__":
    purge_tenant(sys.argv[1])
