def check_system_status(cpu_usage):
    if cpu_usage > 90:
        return "DANGER"

    return "HEALTHY"