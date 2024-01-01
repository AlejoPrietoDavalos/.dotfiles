from typing import List
import subprocess

def desktops_from_ints(desktops: List[int]) -> List[str]:
    return [str(d) for d in desktops]


class CommandsBSPWM:
    @staticmethod
    def set_monitor_primary(monitor: str, pos: str, resolution: str) -> None:
        subprocess.run([
            "xrandr",
            "--output", monitor,
            "--primary",
            "--mode", resolution,
            "--rotate", "normal",
            "--pos", pos
        ])

    @staticmethod
    def set_monitor_secondary(monitor_left: str, monitor_right: str, pos: str, resolution: str) -> None:
        subprocess.run([
            "xrandr",
            "--output", monitor_right,
            "--mode", resolution,
            "--rotate", "normal",
            "--pos", pos,
            "--right-of", monitor_left
        ])

    @staticmethod
    def set_desktops(monitor: str, desktops: List[int]) -> None:
        _command = ["bspc", "monitor", monitor, "-d"]
        _command.extend(desktops_from_ints(desktops))
        subprocess.run(_command)

    @staticmethod
    def set_desktops_from_monitors(monitors: List[str]) -> None:
        if len(monitors) == 1:
            CommandsBSPWM.set_desktops(monitors[0], list(range(1, 10)) + [0])
        if len(monitors) == 2:
            CommandsBSPWM.set_desktops(monitors[0], list(range(1, 5+1)))
            CommandsBSPWM.set_desktops(monitors[1], list(range(6, 9+1)) + [0])


def main(
        monitors: List[str],
        positions: str,
        resolution: str = "1920x1080") -> None:
    CommandsBSPWM.set_monitor_primary(monitors[0], positions[0], resolution)
    for i in range(len(monitors) - 1):
        CommandsBSPWM.set_monitor_secondary(monitors[i], monitors[i+1], positions[i+1], resolution)
    
    CommandsBSPWM.set_desktops_from_monitors(monitors)

if __name__ == "__main__":
    # TODO: Que obtenga los monitores encontrados, y que asigne los desktops dependiendo del número.
    # TODO: Luego hacer una herramienta que permita modificarlos en caso que estén mal asignados.
    monitors = ["HDMI-0", "DP-5"]
    positions = ["0x0", "1920x0"]
    resolution = "1920x1080"
    main(
        monitors = monitors,
        positions = positions,
        resolution = resolution
    )