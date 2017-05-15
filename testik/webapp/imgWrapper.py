import re

text = "Parorm. ![mmmmmmm.jpg](https://steemitimages.com/DQmbYcYhRFuGGdRXPPfvHAymBzDz5Cb4FMYgxEsb6vCUUna/mmmmmmm.jpg) <img src=\"https\" harsh melodic rock with vulnerable, witty lyrics - with singer/songwriter Isaac Brock acting as the common man's David Foster Wallace, delivering succinct & peculiar insights into life that every teenager in America could relate to. As previously mentioned, I posted this list on an old message board nine years ago. This is the revamped & updated version. It doesn't contain songs released after 2008, cuz I don't know the newest album very well. I HOPE YOU ENJOY! please follow me if you do :-) ---"


regex = r'((?<!src=")https?:\/\/[A-Za-z0-9]+.[a-z]{2,3}\/[A-Za-z0-9\/?_?]+.(jpg|gif|png))'

#regex = r'https)'

text = re.sub(regex, r"<img src='\1' />", text)
print(text)




