# Standard
import os

# Third Party
import rumps

# Local
from ilab_bar.command_display_window import CommandDisplayWindow
from ilab_bar.process_monitor import ProcessMonitor
from ilab_bar.configuration_setup import configuration_setup

class InstructLabBarApp(rumps.App):
    """App to run ilab in the macos menu bar"""

    def __init__(self):
        super().__init__(
            name="ilab-bar",
            title="",
            icon=self._resource("ilab.png"),
        )
        # Add start/stop menu
        self._on_icon = self._resource("on.svg")
        self._off_icon = self._resource("off.svg")
        self._menu.add(
            rumps.MenuItem("Start", icon=self._off_icon, callback=self._start_stop)
        )
        self._menu.add(None)

        # Add the output displays
        self._stdout_window = CommandDisplayWindow("stdout")
        self._stdout_menu = rumps.MenuItem("stdout")
        self._stdout_menu.add(self._stdout_window)
        self._stderr_window = CommandDisplayWindow("stderr")
        self._stderr_menu = rumps.MenuItem("stderr")
        self._stderr_menu.add(self._stderr_window)
        self._menu.add(self._stdout_menu)
        self._menu.add(self._stderr_menu)
        self._menu.add(None)

        # Placeholder for the running ilab serve process
        self._ilab_server_proc = None

    def __del__(self):
        if self.running:
            self._start_stop(None)

    @property
    def running(self) -> bool:
        return self._ilab_server_proc is not None

    ##########
    ## Impl ##
    ##########

    _RESOURCE_ROOT = os.path.join(os.path.dirname(__file__), "resources")


    def _start_stop(self, sender: rumps.MenuItem | None) -> None:

        dot_config_path = os.path.join(os.environ.get('HOME'), '.config')
        instruct_config_path = os.path.join(dot_config_path, 'instructlab')
        instruct_config = os.path.join(instruct_config_path, 'config.yaml')

        if self._ilab_server_proc is None:
            if sender is not None:
                sender.title = "Stop"
                sender.icon = self._on_icon

            configuration_setup()

            self._ilab_server_proc = ProcessMonitor(f"cd {instruct_config_path} && instructlab --config={instruct_config} model serve")
            self._stdout_window.set_process(self._ilab_server_proc)
            self._stderr_window.set_process(self._ilab_server_proc)
            self._ilab_server_proc.start()
        else:
            if sender is not None:
                sender.title = "Start"
                sender.icon = self._off_icon
            self._ilab_server_proc.stop()
            self._ilab_server_proc = None

    @classmethod
    def _resource(cls, name: str) -> str:
        return os.path.join(cls._RESOURCE_ROOT, name)
