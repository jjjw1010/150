# Write your MySQL query statement below
select tweet_id
from Tweets
where CHAR_LENGTH(content) > 15
# LENGTH() is diff from CHAR_LENGTH()