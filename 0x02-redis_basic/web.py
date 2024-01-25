import requests
import redis
import functools


redis_client = redis.Redis()


def track_access(method):
    """
    Decorator to track the number of times a particular URL is accessed.
    """
    @functools.wraps(method)
    def wrapper(url, *args, **kwargs):
        access_count_key = f"count:{url}"
        redis_client.incr(access_count_key)

        result = method(url, *args, **kwargs)

        return result

    return wrapper


@track_access
def get_page(url: str) -> str:
    """
    Obtain the HTML content of a particular URL and cache the result
    with an expiration time of 10 seconds.
    """
    cache_key = f"cache:{url}"
    cached_result = redis_client.get(cache_key)

    if cached_result is not None:
        return cached_result.decode('utf-8')

    response = requests.get(url)
    html_content = response.text

    redis_client.setex(cache_key, 10, html_content)

    return html_content
