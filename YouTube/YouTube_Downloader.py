from pytube import YouTube


def Download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print("There has been an error in downloading the youtube video")
    print("This download has completed!!")


link = input("Put your youtube link here!! URL: ")
Download(link)
