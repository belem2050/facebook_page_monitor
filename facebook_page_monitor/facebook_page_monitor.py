import facebook

#This token does not work. It was my used for tesing but I modified it and lect it here so get an idea how it should look like
page_access_token = 'EAAGCrYHozmYBOZCFWjGPCgWgoySgtWgzDTo7l3fpRWiLVQhmNk9TKmm2WWdUdZCoykc1GzaJsaLHfsMVM5Zodhgt5oDxabuIYDgBpWofSw2Abr89DKMGBZAOYNOzeF4GwEtXACcn7GZAAdJZArClsJn0ifQfgGvTMUS74h5vWLWeRg5ZBl3QbAkAP7wHOh4OFbLDneCdq5Uus9JjtTVZCIGSTZBsbucANmfs40LPfNp8ZD'

class FacebookPageMonitor:

    def __init__(self, page_access_token) -> None:

        self.graph = facebook.GraphAPI(page_access_token)

    
    def post_message(self, page_id, connection_name, msg):
        self.graph.put_object(parent_object=page_id, connection_name=connection_name, message=msg)

    def comment_post(self, post_id, msg):
        self.graph.put_comment(object_id=post_id, message=msg)

    def like_post(self, post_id):
        self.graph.put_like(object_id=post_id)

    def uplaod_photo(self, photo_path):
        with open(photo_path, 'rb') as photo:
            self.graph.put_photo(photo)

    def fetch_page_ids(self, user):

        pages = self.graph.get_object(user)

        return pages
    
    def fetch_posts_ids(self, connection_name): # connection names: 'posts', 'photos', 'videos', 'events'
        posts = self.graph.get_connections(id='me', connection_name=connection_name)

        return posts


def main():
    monitor = FacebookPageMonitor(page_access_token)

    page_id = monitor.fetch_page_ids('me')['id']
    
    message = 'There we go, I am posting from a python script to be found on Github'
    monitor.post_message(page_id, 'feed',  message)

    post_id = monitor.fetch_posts_ids('posts')['data'][0]['id'] # JUst to get the latest post
    comment_message = 'A comment from again my python script!\n Life is Great'
    monitor.comment_post(post_id, comment_message)

    monitor.like_post(post_id)

    photo_path = 'data/image.png'

    monitor.uplaod_photo(photo_path)


if __name__=='__main__':
    main()

    