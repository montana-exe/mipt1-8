import os
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def run_script():
    project_root = Path(__file__).parents[1]

    def run(relative_path: str, user_input: str = "", cwd: Path | None = None):
        return subprocess.run(
            [sys.executable, str(project_root / relative_path)],
            input=user_input,
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=True,
            cwd=cwd or project_root,
            env=os.environ | {"PYTHONIOENCODING": "utf-8"},
        )

    return run
