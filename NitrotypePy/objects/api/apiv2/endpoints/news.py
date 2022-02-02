class News:
    def __init__(self):
        self.blogID: int
        self.slug: str
        self.title: str
        self.hasImage: bool
        self.shortBody: str
        self.createdTimestamp: int
        self.lastModified: int
        self.adminID: int
        self.writtenBy: str