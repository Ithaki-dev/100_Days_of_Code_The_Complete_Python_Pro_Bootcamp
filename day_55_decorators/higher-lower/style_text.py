class Stalying:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @staticmethod
    def bold(func):
        def wrapper(*args, **kwargs):
            return f"<b>{func(*args, **kwargs)}</b>"
        return wrapper

    @staticmethod
    def italic(func):
        def wrapper(*args, **kwargs):
            return f"<i>{func(*args, **kwargs)}</i>"
        return wrapper

    @staticmethod
    def underline(func):
        def wrapper(*args, **kwargs):
            return f"<u>{func(*args, **kwargs)}</u>"
        return wrapper

    @staticmethod
    def center(func):
        def wrapper(*args, **kwargs):
            return f"<center>{func(*args, **kwargs)}</center>"
        return wrapper
    