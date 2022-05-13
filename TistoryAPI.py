import requests
import os
from dotenv import load_dotenv
# client_id == app_id
load_dotenv()
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
access_token = os.environ.get("access_token")
redirect_uri = os.environ.get("redirect_uri")

# 인증 요청 및 Authentication code 발급
# https://tistory.github.io/document-tistory-apis/auth/authorization_code.html
def getAuthenticationCode():
    response_type = "code"
    state = "anything"

    url = "https://www.tistory.com/oauth/authorize?" + \
        "client_id="+client_id+"&"+ \
            "redirect_uri=" + redirect_uri + "&"+\
        "response_type=" + response_type + "&"+\
        "state="+state
    return url

# Access Token 발급
# https://tistory.github.io/document-tistory-apis/auth/authorization_code.html
def getAccessToken(code=None):

    code = "9d456e72dbe8fd3b468310028a3055d0212632b25d7c0da2e7beacdee67b830e74132cdd"
    grant_type="authorization_code"

    url = "https://www.tistory.com/oauth/access_token?" +\
        "client_id="+client_id+"&" +\
        "client_secret="+client_secret+"&" +\
        "redirect_uri="+redirect_uri+"&" +\
        "code="+code+"&" +\
        "grant_type="+grant_type

    res = requests.get(url)
    return  res

# 자신의 블로그 정보
# https://tistory.github.io/document-tistory-apis/apis/v1/blog/list.html
def getBlogInfo(output="xml"):
    url = "https://www.tistory.com/apis/blog/info?" +\
        "access_token=" + access_token + "&" +\
        "output=" + output
    res = requests.get(url)
    return res

# 글 목록
# https://tistory.github.io/document-tistory-apis/apis/v1/post/list.html
def getPostList(blogName,page=1, output='xml'):
    url = "https://www.tistory.com/apis/post/list?" + \
          "access_token=" + access_token + "&" + \
          "blogName=" + blogName + "&" + \
          "page=" + str(page) + "&" + \
          "output=" + output
    res = requests.get(url)
    print(res)
    return res

def getCategoryID(blogName, output='xml'):
    url = "https://www.tistory.com/apis/category/list?"

    data = url
    data += "access_token=" + access_token + "&"
    data += "output=" + output + "&"
    data += "blogName=" + blogName

    print(data)
    return requests.get(data)

def postWriting(title="No Title", content="No Content"):
    url = "https://www.tistory.com/apis/post/write?"
    output = "json"
    blogName = "rankdb"

    data = url
    data += "access_token=" + access_token + "&"
    data += "output=" + output + "&"
    data += "blogName=" + blogName + "&"
    data += "title=" + title + "&"
    data += "content=" + content + "&"
    data += "category=1024642"

    print(data)
    return requests.post(data)

