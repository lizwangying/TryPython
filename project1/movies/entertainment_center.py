import media
import fresh_tomatoes

toy_story = media.Movie("Toy_Story","TZeG23jEfHM","http://img4.imgtn.bdimg.com/it/u=2905884479,2990515935&fm=214&gp=0.jpg","https://www.youtube.com/watch?v=TZeG23jEfHM")
zootopia = media.Movie("ZooToPia","jWM0ct-OLsM","http://img5.imgtn.bdimg.com/it/u=1775444780,3096257683&fm=27&gp=0.jpg","https://www.youtube.com/watch?v=jWM0ct-OLsM")
faceOff = media.Movie("FaceOff","BONldMyFHtA","https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=e0d7ad03a2ec08fa320d1bf538875608/d52a2834349b033b4c61f56617ce36d3d439bda4.jpg","https://www.youtube.com/watch?v=BONldMyFHtA")
coco = media.Movie("COCO","OF9Ixfq4BCI","http://www.huarenone.org/images/201711/112710.jpg","https://www.youtube.com/watch?v=OF9Ixfq4BCI")
Up = media.Movie("Up","F2bk_9T482g","http://i1.w.hjfile.cn/slide/201103/Movie%20UP1862197004.jpg","https://www.youtube.com/watch?v=F2bk_9T482g")
BigHero6 = media.Movie("BigHero6","KqFSkylQbEM","http://img4q.duitang.com/uploads/item/201502/10/20150210154014_VrYw4.jpeg","https://www.youtube.com/watch?v=KqFSkylQbEM")
sing = media.Movie("Sing","pHZneOidj9A","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1518118254566&di=64ed71afcab92aaad937dfd996736e09&imgtype=0&src=http%3A%2F%2F2t.5068.com%2Fuploads%2Fallimg%2F161028%2F1-16102P95926-52.jpg","https://www.youtube.com/watch?v=pHZneOidj9A")
padDingTon = media.Movie("PADDINGTON","Ak9VZkdlS9g","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1518152751798&di=411ca703000e084f34618ddea884a9f8&imgtype=0&src=http%3A%2F%2Fimgwx5.2345.com%2Fdypcimg%2Fimg%2F4%2F53%2Fsup161567_223x310.jpg","https://www.youtube.com/watch?v=Ak9VZkdlS9g")
ted2 = media.Movie("ted2","S3AVcCggRnU","https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1518118708594&di=65b9e3125d4428af458a5744de875b88&imgtype=0&src=http%3A%2F%2Fcdn2.52tian.net%2Fdh%2F8779.jpg","https://www.youtube.com/watch?v=S3AVcCggRnU")

movies=[toy_story,zootopia,faceOff,coco,Up,BigHero6,sing,padDingTon,ted2]
fresh_tomatoes.open_movies_page(movies)

boxTitle = "|  movie title  | trailer_youtube_id |"
boxCol1 = "  movie title  "
boxCol2 = "  trailer_youtube_id  "
boxBorder = "-"*len(boxTitle)
print(boxBorder)
print(boxTitle)
for movie in movies:
	spacesNum = (len(boxCol1)-len(movie.title))/2
	spacesNum2 = (len(boxCol2)-len(movie.trailer_youtube_id))/2
	smaces2 = " "*int(spacesNum2)
	spaces = " "*int(spacesNum)
	print("|"+spaces+movie.title+spaces+"|"+smaces2+movie.trailer_youtube_id+smaces2+"|")

print(boxBorder)