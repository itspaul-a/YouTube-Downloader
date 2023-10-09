# Video downloader

from pytube import YouTube

print(r"""
█───█─▄▀▀─█───▄▀▀─▄▀▀▄─█▄─▄█─▄▀▀
█───█─█───█───█───█──█─█▀▄▀█─█──
█───█─█▀▀─█───█───█──█─█─▀─█─█▀▀
█▄█▄█─█───█───█───█──█─█───█─█──
─▀─▀───▀▀──▀▀──▀▀──▀▀──▀───▀──▀▀

        """)

pointer1 = True
p = True

while p:
    while pointer1:
        yt = YouTube(input("Enter Link: "))

        title = yt.title
        print(title)

        ans = input(f"Would you like to download ({title}) y/n?")
        if ans == "y":
            break
        else:
            continue

    print("Downloading...")

    s = yt.streams.get_by_itag(22)
    s.download()

    print("Download complete :)")

    ans2 = input("would you like to download another video? y/n: ")
    if ans2 == "y":
        continue
    else:
        print("Bye!")

        print(r"""\
             _________
            / ======= \
           / __________\
          | ___________ |
          | | -       | |
          | |         | |
          | |_________| |________________________
          |=____________/   Have a good day!     )
          / ::::::::::::\                       /
         / ::::::::::::: \                  =D-'
        (_________________)
                    """)
        break









