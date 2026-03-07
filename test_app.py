import tkinter as tk
from app import ACEestApp

def test_app_initialization():
    root = tk.Tk()
    app = ACEestApp(root)

    # check application object created
    assert app.root is not None

    # check program templates exist
    assert hasattr(app, "program_templates")

    root.destroy()