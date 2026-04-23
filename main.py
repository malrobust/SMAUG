import sys
import os
import yaml
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.spinner import Spinner
from rich.markdown import Markdown
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter

from brain.router import Router
from brain.planner import plan_tasks
from brain.react import ReActEngine
from brain.executor import ToolExecutor
from memory.store import MemoryStore
import logging
from voice.speak import speak
from voice.listen import listen

# Configure Professional Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='sifra.log',
    filemode='a'
)
logger = logging.getLogger("SMAUG")

# Load Config
CONFIG_PATH = "config.yaml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

console = Console()
session = PromptSession(history=FileHistory(os.path.expanduser("~/.jarvis/history")))

def print_header():
    """Renders the professional SIFA platform header."""
    console.print(Panel.fit(
        "[bold orange1]SMAUG[/bold orange1] [white]| Autonomous Assistant & Security Researcher[/white]\n"
        "[dim]Agent: Livion | Mode: Active | Version: 1.0.0[/dim]",
        border_style="orange1"
    ))

def main_loop():
    """Main execution loop for the Smaug Autonomous Security Platform."""
    logger.info("Initializing Smaug execution loop.")
    router = Router(model=config['ollama']['model'])
    engine = ReActEngine(model=config['ollama']['model'])
    executor = ToolExecutor()
    memory = MemoryStore()
    
    print_header()
    
    voice_mode = config['ui'].get('voice_enabled', False)
    
    slash_commands = WordCompleter(["/voice", "/clear", "/session", "/help", "/exit"])

    while True:
        try:
            if config.get('voice_mode', False):
                user_input = listen()
                console.print(f"[bold orange1]User (Voice):[/bold orange1] {user_input}")
            else:
                user_input = session.prompt("smaug > ", completer=slash_commands)
            
            if not user_input.strip():
                continue

            # Command Handling
            if user_input.startswith("/"):
                cmd = user_input.split()[0]
                if cmd == "/exit":
                    break
                elif cmd == "/clear":
                    console.clear()
                    print_header()
                    continue
                elif cmd == "/voice":
                    voice_mode = not voice_mode
                    console.print(f"[bold yellow][*] Voice mode set to {voice_mode}[/bold yellow]")
                    continue
                elif cmd == "/help":
                    console.print("[bold cyan]Commands:[/bold cyan] /voice, /clear, /session, /help, /exit")
                    continue
            
            # Step 1: Routing
            with console.status("[bold blue]Routing intent...", spinner="dots"):
                route_result = router.route(user_input)
            
            mode = route_result.get("mode", "general")
            intent = route_result.get("intent", "unknown")
            logger.info(f"Routed intent: {intent} in mode: {mode}")
            
            console.print(f"[dim][*] Mode: {mode} | Intent: {intent}[/dim]")
            
            # Step 2: Planning
            with console.status("[bold purple]Decomposing tasks...", spinner="bouncingBar"):
                tasks = plan_tasks(user_input, mode, route_result.get("args", {}))
            
            # Step 3: Execution Loop
            for i, task in enumerate(tasks):
                console.print(Panel(f"[bold]Task {i+1}:[/bold] {task}", border_style="blue"))
                
                # ReAct Streaming Output
                with Live(console=console, refresh_per_second=4) as live:
                    live.update(Spinner("dots", text="[bold yellow]Agent Thinking..."))
                    
                    final_answer = ""
                    for update in engine.run_stream(mode, task, executor, executor.get_all_descriptions()):
                        if "thought" in update:
                            live.update(Panel(f"[white]{update['thought']}[/white]", title="Thinking", border_style="yellow"))
                        elif "action" in update:
                            live.update(Panel(f"[cyan]Action:[/cyan] {update['action']['name']}\n[dim]{update['action'].get('args', {})}[/dim]", title="Action", border_style="cyan"))
                        elif "observation" in update:
                            live.update(Panel(f"[green]Result:[/green]\n{str(update['observation'])[:500]}...", title="Observation", border_style="green"))
                        elif "final_answer" in update:
                            final_answer = update['final_answer']
                            
                    if final_answer:
                        live.update(Panel(Markdown(final_answer), title="Final Answer", border_style="green"))
                        if mode == "security":
                            memory.store(f"task_{i}", final_answer)
                        if voice_mode:
                            speak(final_answer)

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red][!] Error:[/bold red] {e}")

if __name__ == "__main__":
    main_loop()
