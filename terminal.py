# terminal.py

import os

def create_terminal_directory():
    """
    Erstellt den Ordner .terminal, wenn er nicht existiert.
    """
    if not os.path.exists('.terminal'):
        os.makedirs('.terminal')

def clear_screen():
    """
    Löscht den Bildschirm.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def list_directory():
    """
    Listet den Inhalt des aktuellen Verzeichnisses auf.
    """
    files = os.listdir('.')
    print("\n".join(files))

def make_directory(directory_name):
    """
    Erstellt einen neuen Ordner mit dem angegebenen Namen.
    """
    os.makedirs(directory_name)

def create_file(file_name):
    """
    Erstellt eine neue Datei mit dem angegebenen Namen.
    """
    with open(file_name, 'w') as file:
        pass

def change_directory(directory_name):
    """
    Wechselt das aktuelle Verzeichnis.
    """
    os.chdir(directory_name)

def backup_files():
    """
    Sichert alle Dateien und Ordner in das .terminal-Verzeichnis.
    """
    files = os.listdir('.')
    terminal_dir = '.terminal'
    for file in files:
        if file != terminal_dir:
            os.replace(file, os.path.join(terminal_dir, file))

def go_back():
    """
    Wechselt zum vorherigen Verzeichnis.
    """
    os.chdir('.terminal')

# Grundlegende Befehle und zugehörige Funktionen
commands = {
    'clear': clear_screen,
    'exit': exit,
    'ls': list_directory,
    'mkdir': make_directory,
    'file': create_file,
    'cd': change_directory,
    'bib': backup_files,
    'go': go_back
}

def start_terminal(prompt):
    """
    Startet einen interaktiven Terminal mit den grundlegenden Befehlen.

    Args:
        prompt (str): Der Prompt, der im Terminal angezeigt wird.
    """
    create_terminal_directory()
    while True:
        user_input = input(prompt)
        command, *args = user_input.split()
        if command.lower() == 'exit':
            break
        elif command in commands:
            try:
                commands[command](*args)
            except TypeError:
                print("Falsche Anzahl an Argumenten für den Befehl.")
        else:
            print("Ungültiger Befehl. Verfügbare Befehle:", list(commands.keys()))

if __name__ == "__main__":
    start_terminal(">> ")
