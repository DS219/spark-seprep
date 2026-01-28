## Simple Vim Tutorial

Vim is a powerful text editor that runs in the terminal. It has two main modes: **Normal Mode** (for navigation and commands) and **Insert Mode** (for typing text).

### Opening and Closing Files

1. **Open a file with Vim**:
   ```bash
   vi practice.txt
   ```
   When you open Vim, you start in Normal Mode.

2. **Close Vim without saving**:
   - Press `Esc` to make sure you're in Normal Mode
   - Type `:q!` and press Enter
   - The `!` forces Vim to quit without saving changes

3. **Save and close Vim**:
   - Press `Esc` to make sure you're in Normal Mode
   - Type `:wq` and press Enter
   - `w` means write (save), `q` means quit

4. **Save without closing**:
   - Press `Esc` to make sure you're in Normal Mode
   - Type `:w` and press Enter

### Switching Between Modes

**Normal Mode** → **Insert Mode**:
- Press `i` to insert text at the cursor position
- Press `o` to open a new line below the cursor and enter Insert Mode
- Press `O` (capital O) to open a new line above the cursor and enter Insert Mode

**Insert Mode** → **Normal Mode**:
- Press `Esc` to return to Normal Mode

### Basic Editing in Normal Mode

When you're in Normal Mode (not typing text), you can use these commands:

- **Delete a line**: Press `dd` to delete the entire line where your cursor is
- **Undo**: Press `u` to undo your last change
- **Move cursor**: Use arrow keys or `h` (left), `j` (down), `k` (up), `l` (right)

### Practice Exercise

1. Open a new file:
   ```bash
   vi practice.txt
   ```

2. Press `i` to enter Insert Mode and type:
   ```
   This is my first line.
   ```

3. Press `Esc` to return to Normal Mode.

4. Press `o` to open a new line below and automatically enter Insert Mode. Type:
   ```
   This is my second line.
   ```

5. Press `Esc` to return to Normal Mode.

6. Press `O` (capital O) to open a new line above. Type:
   ```
   This line goes above!
   ```

7. Press `Esc` to return to Normal Mode.

8. Use arrow keys to move your cursor to the second line.

9. Press `dd` to delete that line.

10. Press `u` to undo the deletion.

11. Save and quit by typing `:wq` and pressing Enter.

### Quick Reference

| Action | Command |
|--------|---------|
| Enter Insert Mode (at cursor) | `i` |
| Enter Insert Mode (new line below) | `o` |
| Enter Insert Mode (new line above) | `O` |
| Exit Insert Mode | `Esc` |
| Delete current line | `dd` |
| Undo | `u` |
| Save | `:w` |
| Quit without saving | `:q!` |
| Save and quit | `:wq` |

### Tip
You can always tell if you're in Insert Mode by looking at the bottom of the screen. If you see `-- INSERT --`, you're in Insert Mode. If you don't see anything, you're in Normal Mode.
