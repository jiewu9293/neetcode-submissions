class Twitter:

    def __init__(self):
        # Global timestamp used to determine tweet order
        self.time = 0

        # user_id -> list of (timestamp, tweet_id)
        self.tweets = defaultdict(list)

        # follower_id -> set of followee_ids
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store the tweet with the current timestamp
        self.tweets[userId].append((self.time, tweetId))
        # Increase the timestamp for the next tweet
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []
        # The news feed includes the user's own tweets
        users = self.following[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                timestamp, tweet_id = self.tweets[uid][index]

                heapq.heappush(
                    max_heap,
                    (-timestamp, tweet_id, uid, index)
                )
        # Extract at most 10 newest tweets
        # root of the maxheap is the most recent tweet
        while max_heap and len(result) < 10:
            neg_time, tweet_id, uid, index = heapq.heappop(max_heap)
            result.append(tweet_id)

            # Add the previous tweet from the same user
            previous_index = index - 1

            if previous_index >= 0:
                timestamp, previous_tweet_id = self.tweets[uid][previous_index]

                heapq.heappush(
                    max_heap,
                (-timestamp,previous_tweet_id,uid,previous_index)
                )
        return result



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
