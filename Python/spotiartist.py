#!/usr/bin/env python

'''
script to directly open a spotify artist page from command line
'''

#/- Importing Requests to request the API,
#/- OS to run OS Commands,
#/- sys to get arguments and
#/- getopt to get the option chosen by the user in arguments

import requests,os,getopt,sys

#/- Unpacking Arguments using getopt to get the artist name
opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])

#/- "track" here refers to the artist's name
track = ''

for i in args:
	#/- sometimes, artist names may be 2 or more words, hence concatenating
	#/- every argument into one artist name
	track += i

#/- using a free version of the Spotify API to look up
#/- artists matching the name
uris = requests.get(f"https://elegant-croissant.glitch.me/spotify?q={track}&type=artist").json()["artists"]["items"]

#/- initializing a counter variable 'c'
c=0

for i in uris:

	#/- 'c' counter variable keeps track of the loop index
	c+=1

	#/- displaying the artist name to the user, listing the
	#/- options they have
	print(c,i["name"])

#/- prompting the user to choose an option by the counter variable//loop index
opn = input('OPTION : ')

#/- getting Spotify's URI code for the chosen artist
uri = uris[int(opn)-1]["uri"]

#/- getting Spotify's WebApp link/URL for the chosen artist
url = uris[int(opn)-1]["external_urls"]["spotify"]


#/- checking if os is windows or others:

if os.name == 'nt': #/- 'nt' is the code for Windows
	from webbrowser import open as opn; opn(url) #/- opening the spotify link

else:

	#/- most other systems (linux and mac) use
	#/- bash and hence are assumed to have playerctl
	#/- installed to control the music player//spotify player

	os.system(f"playerctl open {uri}")

#/- fallback in case the url was not opened

print(f"Visit:\n\n{url}\n\nif the Artist Page was not opened automatically.")

'''
SCRIPT BY AADITYARENGARAJAN (GitHub @aadityarengarajan or https://aaditya.intellx.co.in)

Script to Automatically Play a Spotify Artist using PlayerCTL//WebBrowser.
'''
