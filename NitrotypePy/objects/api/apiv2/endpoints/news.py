from typing import TypedDict


News = TypedDict(
    "News",
    {
        "blogID": int,
        "slug": str,
        "title": str,
        "hasImage": bool,
        "shortBody": str,
        "createdTimestamp": int,
        "lastModified": int,
        "adminID": int,
        "writtenBy": str,
    },
)
