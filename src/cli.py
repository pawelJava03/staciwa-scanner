from branding import show_welcome
from rich.style import Style
from rich.text import Text
from rich.console import Console
console = Console()
from branding import build_colored_text as bct

def main():
    show_welcome()


    while True:
        command = input("\n[staciwa] > ").strip().lower()
        if command == 'help':
            print("Available commands:")
            print("Available commands:")
            print(f"  help - show this help message\n")
            print(f"  scan <url> - scan a website for vulnerabilities\n")
            print(f"  exit - exit the application\n")

        elif command.startswith('scan'):
            url = command.split(" ")[1] if len(command.split()) > 1 else None
            if url:
                print(f"Scanning {url}...")
            else:
                print("Please provide a URL to scan.")
        elif command == 'exit':

            console.print(bct('Goodbye! Thank you for using Staciwa Scanner!'))
            break
        else:
            print(f"Unknown command: {command}\n")
            print(f"Please try again.")
            print("For help, type 'help'")

if __name__ == "__main__":
    main()
