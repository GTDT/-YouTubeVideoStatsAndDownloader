from pytube import YouTube as YT
import time

URL = input("Enter YouTube URL: ")
Video = YT(URL)

print("\n\nVideo Title: ", Video.title,"\n\nVideo Views: ", Video.views,"\n\nVideo length: ", Video.length,"seconds\n\nVideo rating: ", Video.rating)

print("\n\n",Video.streams.filter(progressive=True),"\n\n")

VideoStreams = Video.streams.get_highest_resolution()

print("Downloading")
VideoStreams.download()
print("Download is Done")

time.sleep(10)

#exec("""\nfrom pytube import YouTube as YT\nimport time\nURL = input("Enter YouTube URL: ")\nVideo = YT(URL)\n\nprint("\\n\\nVideo Title: ", Video.title,"\\n\\nVideo Views: ", Video.views,"\\n\\nVideo length: ", Video.length,"seconds\\n\\nVideo rating: ", Video.rating)\n\nprint("\\n\\n",Video.streams.filter(progressive=True),"\\n\\n")\n\nVideoStreams = Video.streams.get_highest_resolution()\n\nprint("Downloading")\nVideoStreams.download()\nprint("Download is Done")\ntime.sleep(10)""")