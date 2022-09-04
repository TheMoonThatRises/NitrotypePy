from typing import TypedDict


News = TypedDict(
    "News",
    {
        "blogID": int,
        "slug": str,
        "title": str,
        "hasImage": bool,
        "createdTimestamp": int,
        "lastModified": int,
        "adminID": int,
        "writtenBy": str,
        "shortBody": str,
        "body": str,
    },
)
