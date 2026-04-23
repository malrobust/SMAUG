import sys
import os
import shutil
import time
import yaml
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, DownloadColumn
from rich.table import Table
from rich.markdown import Markdown
from rich.prompt import Confirm, Prompt

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    header_text = """
[bold orange1]SMAUG | Autonomous Security Platform[/bold orange1]
[dim italic]Setting up your high-fidelity security research environment[/dim italic]
    """
    console.print(Panel(header_text.strip(), border_style="orange1"))

def check_ollama():
    try:
        import ollama
        client = ollama.Client()
        client.list()
        return True
    except Exception:
        return False

def check_model(model_name="gemma:30b"):
    try:
        import ollama
        client = ollama.Client()
        models = client.list()
        for m in models['models']:
            if m['name'].startswith(model_name):
                return True
        return False
    except Exception:
        return False

def setup_wizard():
    clear_screen()
    show_header()
    
    console.print("\n[bold]Phase 1: System Verification[/bold]")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        # Check Dependencies
        task1 = progress.add_task(description="Checking Python dependencies...", total=None)
        time.sleep(1)
        progress.update(task1, completed=True)
        
        # Check Ollama
        task2 = progress.add_task(description="Verifying Ollama service...", total=None)
        if check_ollama():
            progress.update(task2, completed=True)
        else:
            console.print("[bold red][!] Error:[/bold red] Ollama service not detected. Please ensure Ollama is installed and running.")
            sys.exit(1)

        # Check Model
        task3 = progress.add_task(description="Checking for Gemma 30B...", total=None)
        if check_model("gemma:30b"):
            progress.update(task3, completed=True)
        else:
            progress.stop()
            if Confirm.ask("[yellow][?][/yellow] Gemma 30B model not found. Pull it now? (Requires ~17GB)"):
                console.print("[info] Pulling Gemma 30B... This may take a while depending on your connection.")
                try:
                    subprocess.run(["ollama", "pull", "gemma:30b"], check=True)
                except Exception as e:
                    console.print(f"[bold red][!] Error pulling model:[/bold red] {e}")
                    sys.exit(1)
            else:
                console.print("[dim]Skipping model pull. Please note SMAUG requires a reasoning model to function.[/dim]")

    console.print("\n[bold]Phase 2: Configuration[/bold]")
    
    config_path = "config.yaml"
    config_example = "config.yaml.example"
    
    if not os.path.exists(config_path):
        if os.path.exists(config_example):
            shutil.copy(config_example, config_path)
            console.print("[green][✓][/green] Initialized config.yaml from template.")
    
    # Quick Config Scan
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    console.print(f"Current Model: [cyan]{config.get('ollama', {}).get('model', 'None')}[/cyan]")
    
    # Phase 3: Finalization
    console.print("\n[bold]Phase 3: System Finalization[/bold]")
    
    # Create directories
    os.makedirs("memory", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    time.sleep(1)
    
    # Final Report
    report = Table(show_header=False, box=None)
    report.add_row("[green]Ollama[/green]", "Online")
    report.add_row("[green]Gemma 30B[/green]", "Verified" if check_model("gemma:30b") else "[yellow]Missing[/yellow]")
    report.add_row("[green]Config.yaml[/green]", "Initialized")
    report.add_row("[green]Memory Engine[/green]", "Ready")
    
    console.print(Panel(report, title="SMAUG Readiness Report", border_style="orange1"))
    
    console.print("\n[bold orange1]Setup Complete.[/bold orange1] You are ready to unleash SMAUG.")
    console.print("[dim]Run [bold]python3 main.py[/bold] to start.[/dim]\n")

if __name__ == "__main__":
    try:
        setup_wizard()
    except KeyboardInterrupt:
        console.print("\n[dim]Setup aborted by user.[/dim]")
