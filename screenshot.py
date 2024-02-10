from pathlib import Path
import os

path_screens = Path.home() / "images" / "screenshots"
path_tmp = Path.home() / ".config" / "qtile" / ".tmp"
path_tmp_screen = path_tmp / "tmp_screenshot.png"

n_screens = [int(screenshot.stem) for screenshot in path_screens.iterdir()]     # Poner que verifique si el string es un entero o no.
idx_max_screen = max(n_screens) if len(n_screens)!=0 else 0

path_out = path_screens / f'{idx_max_screen + 1}.png'
os.system(f"scrot -q 100 -f -s {path_out}")
os.system(f"xclip -selection clipboard -t image/png -i {path_out}")
path_out.unlink()
