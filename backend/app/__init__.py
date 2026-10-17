import sys
import io

# Ensure UTF-8 encoding on Windows consoles to prevent UnicodeEncodeError with emojis/box characters
if sys.platform == "win32":
    if sys.stdout and hasattr(sys.stdout, "buffer") and not getattr(sys.stdout, "closed", False):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            try:
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
            except Exception:
                pass
    if sys.stderr and hasattr(sys.stderr, "buffer") and not getattr(sys.stderr, "closed", False):
        try:
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            try:
                sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
            except Exception:
                pass
