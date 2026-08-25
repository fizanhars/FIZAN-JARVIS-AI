import platform
import shutil


def system_info() -> dict:
    """Return basic information about the current system."""
    total, used, free = shutil.disk_usage("/")

    return {
        "platform": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "disk_free_gb": round(free / (1024 ** 3), 2),
    }


if __name__ == "__main__":
    info = system_info()

    for key, value in info.items():
        print(f"{key}: {value}")
