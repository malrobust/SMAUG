from ..system.shell import run_command

def run_nmap(target):
    """
    Port scanning using nmap.
    """
    cmd = f"nmap -sV {target}"
    return run_command(cmd)

def run_nuclei(target):
    """
    Vulnerability scanning using Nuclei.
    """
    cmd = f"nuclei -u {target}"
    return run_command(cmd)

def run_ffuf(url, wordlist="/usr/share/wordlists/dirb/common.txt"):
    """
    Directory fuzzing using ffuf.
    """
    cmd = f"ffuf -u {url}/FUZZ -w {wordlist}"
    return run_command(cmd)
