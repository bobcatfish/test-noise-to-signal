import functools

import icecream


def retry(retries):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            for i in range(retries+1):
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    if i == retries:
                        raise Exception(
                            "still failing after {} retries: {}".format(i, e))
        return wrapper_retry
    return decorator_retry


def retry_network_errors(f, retries):
    for i in range(retries+1):
        try:
            f()
        except icecream.NetworkException as e:
            if i == retries:
                raise Exception(
                    "still failing after {} retries: {}".format(i, e))
        else:
            return
