import TistoryAPI as t
import json

if __name__ == "__main__":
    #token = getAccessToken().content
    #print(token.decode('utf-8'))

    #category = json.loads(getCategoryID("rankdb").content)
    #category = json.dumps(category, ensure_ascii=False)
    #print(category)

    post_list = json.loads(t.getPostList("rankdb",page=1,output='json').content)
    post_list = json.dumps(post_list, ensure_ascii=False)
    print(post_list)

    #getAuthenticationCode()
    #posting = json.loads(postWriting(title="Test Title", content="Test Content").content)
    #print(posting)