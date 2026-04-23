from ..system.shell import run_command

def run_amass(target):
    """
    Subdomain enumeration using Amass.
    """
    cmd = f"amass enum -d {target}"
    return run_command(cmd)

def run_httpx(target):
    """
    Live host and tech detection using httpx.
    """
    cmd = f"echo {target} | httpx -td -title"
    return run_command(cmd)

def run_whatweb(target):
    """
    Technology stack fingerprinting.
    """
    cmd = f"whatweb {target}"
    return run_command(cmd)
