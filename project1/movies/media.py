# coding=utf-8
import webbrowser


class Movie(object):
    """movie class, 含有 title，trailer_youtube_id,
    trailer_youtube_id,trailer_youtube_url属性变量
    """

    def __init__(self, title, trailer_youtube_id,
                 poster_image_url, trailer_youtube_url):
        """初始化变量"""
        super(Movie, self).__init__()
        self.title = title
        self.trailer_youtube_id = trailer_youtube_id
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """打开播放器，播放电影预告片"""
        webbrowser.open(self.trailer_youtube_url)
