import curses


class InterfaceManager:
    def __init__(self, game_state, send_message):
        self.game_state = game_state
        self.send_message = send_message

    def run(self, stdscr):
        input_buffer = ""
        messages = []

        try:
            while True:
                # Display data at the top
                stdscr.move(0, 0)
                data = self.game_state.read_data()
                stdscr.addstr(data)
                
                # Display past messages
                for i, msg in enumerate(messages):
                    stdscr.move(i + 1, 0)
                    stdscr.clrtoeol()
                    stdscr.addstr(f"you: {msg}")

                # Text prompt and current input
                stdscr.move(len(messages) + 1, 0)
                stdscr.clrtoeol()
                stdscr.addstr(f"> {input_buffer}")
                
                c = stdscr.getch()
                
                if c == 3:  # Ctrl+C
                    break
                elif c == 10:  # Enter key
                    if input_buffer:
                        messages.append(input_buffer)
                    input_buffer = ""
                    
                    # Check for quit command
                    if input_buffer.lower() == 'q':
                        break
                elif c >= 32 and c <= 126:  # Printable characters
                    input_buffer += chr(c)

                stdscr.refresh()

        except KeyboardInterrupt:
            pass
        finally:
            # Cleanup
            curses.endwin()
