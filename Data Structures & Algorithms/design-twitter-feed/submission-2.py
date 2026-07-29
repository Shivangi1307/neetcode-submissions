from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetMap[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:

        result = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:

            if followee in self.tweetMap:

                index = len(self.tweetMap[followee]) -1 

                time,tweet = self.tweetMap[followee][index]

                heapq.heappush(heap,(-time,tweet,followee,index-1))

        while heap and len(result) < 10:

            negtime,tweet,followee,index = heapq.heappop(heap)
            result.append(tweet)

            if index >= 0:
                time,nextTweet = self.tweetMap[followee][index]

                heapq.heappush(heap,(-time,nextTweet,followee,index-1))

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
