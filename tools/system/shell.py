import subprocess

def run_command(command, timeout=30):
    """
    Executes a shell command and returns the output.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "status": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {"error": "Command timed out."}
    except Exception as e:
        return {"error": str(e)}

def kill_port(port):
    """
    Kills any process using the specified port.
    """
    cmd = f"fuser -k {port}/tcp"
    return run_command(cmd)

def list_processes():
    """
    Lists running processes.
    """
    cmd = "ps aux --sort=-%cpu | head -n 11"
    return run_command(cmd)
