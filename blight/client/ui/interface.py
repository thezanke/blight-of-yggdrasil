import curses


class InterfaceManager:
    def __init__(self, game_state, send_message):
        self.game_state = game_state
        self.send_message = send_message

    def run(self, stdscr):
        # Initialize curses environment
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        try:
            while True:
                stdscr.clear()
                data = self.game_state.read_data()
                stdscr.addstr(0, 0, data)
                stdscr.refresh()
                
                
                # Capture user input
                user_input = stdscr.getstr(1, 0).decode('utf-8')
                
                # Clear the current input line
                stdscr.deleteln()
        
                # Check for quit command
                if user_input.lower() == 'q':
                    break

                # Display user input
                stdscr.addstr(2, 0, f"You entered: {user_input}      ")  # Extra spaces to clear previous text
                stdscr.refresh()
                
        finally:
            # Cleanup
            curses.endwin()
