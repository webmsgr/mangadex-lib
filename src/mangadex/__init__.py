import cfscrape


class Manga:
    def __init__(self, id, downloadInfo=True, DownloadChapterInfo=False):
        self.id = id
        self.download = downloadInfo
        self.title = None
        self.description = None
        self.artist = None
        self.author = None
        self.chapters = None
        self.scraper = cfscrape.create_scraper()
        if self.download:
            self.downloadinfo(DownloadChapterInfo)

    def downloadinfo(self, downloadChapters=False):
        self.rawjson = self.scraper.get(
            "https://mangadex.org/api/manga/{}".format(self.id)).json()
        self.json = self.rawjson["manga"]
        self.title = self.json["title"]
        self.description = self.json["description"]
        self.artist = self.json["artist"]
        self.author = self.json["author"]
        chapters = [
            Chapter(x, downloadChapters, self.scraper)
            for x in self.rawjson["chapter"]
        ]
        if not downloadChapters:
            for chapter in chapters:
                chapter.json = self.rawjson["chapter"][chapter.id]
                chapter._populate(False)
        self.chapters = {}
        for chapter in chapters:
            if chapter.chapter not in self.chapters:
                self.chapters[chapter.chapter] = {}
            if chapter.lang not in self.chapters[chapter.chapter]:
                self.chapters[chapter.chapter][chapter.lang] = []
            self.chapters[chapter.chapter][chapter.lang].append(chapter)


class Chapter:
    def __init__(self,
                 id,
                 downloadInfo=True,
                 scraper=cfscrape.create_scraper()):
        self.id = id
        self.scraper = scraper
        self.json = {}
        if downloadInfo:
            self.downloadcontent()

    def downloadcontent(self):
        self.json = self.scraper.get(
            "https://mangadex.org/api/chapter/{}".format(self.id)).json()
        self._populate(True)

    def _populate(self, isTarget=False):
        self.volume = self.json["volume"]
        self.chapter = self.json["chapter"]
        self.lang = self.json["lang_code"]
        self.title = self.json["title"]
        self.group_id = self.json["group_id"]
        self.group_name = self.json["group_name"]
        self.pages = []
        if isTarget:
            self.hash = self.json["hash"]
            self.server = self.json["server"]
            if "mangadex.org" not in self.server:
                self.server = "https://mangadex.org" + self.server
            self.pages = [
                self.server + self.hash + "/" + x
                for x in self.json["page_array"]
            ]


def getmangachapter(mangaid, langcode, chapnum, getpages=False):
    man = Manga(mangaid, True, getpages)
    chap = man.chapters[chapnum][langcode][0]
    return chap


def getmangachapters(mangaid, langcode, chapnums, getpages=False):
    return [
        getmangachapter(mangaid, langcode, str(x), getpages) for x in chapnums
    ]


def test(mangaid=16617, langcode="gb"):
    chaps = getmangachapters(mangaid, langcode, [1, 2], True)
    return [x.pages for x in chaps]


test()
