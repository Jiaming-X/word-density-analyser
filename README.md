# word-density-analyser

### example commands, and their results:
```sh
python main.py "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/" 
```
Scores | topics
------ | -------------
11.2  |  edward snowden
10.6  |  edward snowden live
10.6  |  snowden live
10.6  |  surveillance program
10.6  |  leaks safeguard
```sh
python main.py "http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster"
```
Scores | topics
------ | -------------
14.8  |  cuisinart cpt-122
14.8  |  compact plastic toaster
14.8  |  plastic toaster
14.8  |  compact plastic
14.2  |  compact plastic toaster (white)

```sh
python main.py "http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/"
```
Scores | topics
------ | -------------
11.8  |  friend outdoors
11.8  |  introduce indoorsy friend outdoors
11.8  |  introduce indoorsy friend
11.8  |  introduce indoorsy
11.8  |  indoorsy friend

### Design:
main.py : the main function that organize the programs

htmlPage.py : use the url to request the webpage, and parse its key attributes: body, title, metadata 

ngram_processor.py : use n-gram algorithm to calcuate the corresponding scores, and choose the ones with top scores 
