import cfscrape
class Manga(): 
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
        self.rawjson = self.scraper.get("https://mangadex.org/api/?id={}&type=manga".format(self.id)).json()
        self.json = self.rawjson["manga"]
        self.title = self.json["title"]
        self.description = self.json["description"]
        self.artist = self.json["artist"]
        self.author = self.json["author"]
        chapters = [Chapter(x, self.rawjson["chapter"][x], downloadChapters, self.scraper) for x in self.rawjson["chapter"]]
        self.chapters = {}
        for chapter in chapters:
            if chapter.chapter not in self.chapters:
                self.chapters[chapter.chapter] = {}
            if chapter.lang not in self.chapters[chapter.chapter]:
                self.chapters[chapter.chapter][chapter.lang] = []
            self.chapters[chapter.chapter][chapter.lang].append(chapter)


class Chapter():
    def __init__(self, id, json, download=False, scraper=cfscrape.create_scraper()):
        self.json = json
        self.id = id
        self.volume = self.json["volume"]
        self.chapter = self.json["chapter"]
        self.lang = self.json["lang_code"]
        self.title = self.json["title"]
        self.group_id = self.json["group_id"]
        self.group_name = self.json["group_name"]
        self.scraper = scraper
        self.pages = []
        if download:
            self.getpages()
    def getpages(self):
        downloadedjson = self.scraper.get("https://mangadex.org/api/?id={}&type=chapter".format(self.id)).json()
        self.hash = downloadedjson["hash"]
        self.server = downloadedjson["server"]
        if self.server == "/data/":
            self.server = "https://mangadex.org/data/"
        self.pages = [self.server+self.hash+"/"+x for x in downloadedjson["page_array"]]
def getchapter(mangaid, langcode, chapnum, getpages=False):
    man = Manga(mangaid)
    chap = man.chapters[chapnum][langcode][0]
    if getpages:
        chap.getpages()
    return chap
def getchapters(mangaid, langcode, chapnums, getpages=False):
    return [getchapter(mangaid, langcode, x, getpages) for x in chapnums]
def test(mangaid=16617, langcode="gb"):
    chaps = getchapters(mangaid, langcode, ["1", "2"], True)
    return [x.pages for x in chaps]
def chapterfromid(id, getpages=False):
    jsn = cfscrape.create_scraper().get("https://mangadex.org/api/?id={}&type=chapter".format(id)).json()
    mangaid = jsn["manga_id"]
    chapter = jsn["chapter"]
    langcode = jsn["lang_code"]
    return getchapter(mangaid, langcode, chapter, getpages)

test()
