# -- coding: UTF-8 --

from console_configs import ConsoleConfigs
from wii_file_exporter import WiiFileExporter


if __name__ == "__main__":
    old_storage_device_code = ConsoleConfigs.set_storage_device_code(
        ConsoleConfigs.STORAGE_SD
    )
    # WiiFileExporter("FB Alpha 2012 CPS-3").run()
    # WiiFileExporter("JoJo's Venture").run()
    # WiiFileExporter("JoJo's Venture 2").run()
    # WiiFileExporter("Street Fighter 3").run()
    # WiiFileExporter("Street Fighter 3.2").run()
    # WiiFileExporter("Street Fighter 3.3").run()
    WiiFileExporter().run()
    ConsoleConfigs.set_storage_device_code(old_storage_device_code)
