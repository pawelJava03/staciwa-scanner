from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.console import Console
from rich.style import Style


def build_colored_text(text):
    colors = ["magenta", "violet", "blue", "cyan"]
    styled_text = Text(justify="center")

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        styled_text.append(char, style=Style(color=color, bold=True))

    return styled_text


def show_welcome():
    console = Console()
    logo = """
███████╗████████╗ █████╗  ██████╗██╗██╗   ██╗ █████╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║██║   ██║██╔══██╗
███████╗   ██║   ███████║██║     ██║██║   ██║███████║
╚════██║   ██║   ██╔══██║██║     ██║╚██╗ ██╔╝██╔══██║
███████║   ██║   ██║  ██║╚██████╗██║ ╚████╔╝ ██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝  ╚═╝  ╚═╝
    """


    console.print(Panel.fit(Text(logo, justify="center"), border_style="bright_cyan"))
    console.print(build_colored_text("Staciwa: Narzędzie CLI do skanowania bezpieczeństwa stron"))
