import sys
import io

# Ensure UTF-8 output encoding on Windows consoles
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

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
