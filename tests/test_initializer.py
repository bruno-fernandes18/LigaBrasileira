import os
import sys
import types

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from brasileirao.gui.initializer import _enforce_ratio

class FakeWidget:
    def winfo_toplevel(self):
        return object()

class FakeEvent:
    def __init__(self, width=100, height=100):
        self.width = width
        self.height = height
        self.widget = FakeWidget()

# Ensure function does not raise when geometry is unsupported

def test_enforce_ratio_no_geometry(caplog):
    event = FakeEvent()
    _enforce_ratio(event)
    assert any('não suporta geometry' in msg for msg in caplog.text.splitlines())
