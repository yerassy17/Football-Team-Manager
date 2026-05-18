def team_info(func):
    def wrapper(*args, **kwargs):
        print("\n--- Team Statistics ---")
        return func(*args, **kwargs)
    return wrapper