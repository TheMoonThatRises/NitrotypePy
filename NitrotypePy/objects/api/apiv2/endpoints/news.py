from typing import TypedDict


class News(TypedDict):
    blogID: int
    slug: str
    title: str
    hasImage: bool
    shortBody: str
    createdTimestamp: int
    lastModified: int
    adminID: int
    writtenBy: str
