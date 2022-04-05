# Have you ever went to Twitter just to make one single post and then find yourself scrolling for 20 minutes and still haven't made a post
# No worries thats why I made the Remote Twitter Poster (RTP)

# This app is linked to the Twitter Account @API_Dummy all tweets will be posted on that account


from request_api import my_Twitter

# ENDPOINTS
_tweets_endpoint = "https://api.twitter.com/2/tweets"
_users_endpoint = "https://api.twitter.com/2/users"
_id_by_username_endpoint ="https://api.twitter.com/2/users/by/username"

# PRIVATE KEYS
# Unique identifier to Twitter account @API_Dummy 
_Bearer_Token = 'Bearer AAAAAAAAAAAAAAAAAAAAAKhhbAEAAAAAbzUznYMeBMIQTCswC8LaeNlC6FA%3D4vaJGGYanVdMJrDi5RsGZBFRyxB1PbtkznoZPVYub5AtggE8nV'

# HEADER AUTHORIZATION 
# Unique to 
_get_header_authorization = {
  'Authorization': _Bearer_Token,
  'Cookie': 'guest_id=v1%3A164898541786063391; guest_id_ads=v1%3A164898541786063391; guest_id_marketing=v1%3A164898541786063391; personalization_id="v1_o5S6QbN0L1U1c9hLRaL7VQ=="' 
  }


_dummy_post_header_authorization = {
     'Authorization': 'OAuth oauth_consumer_key="JL1wH9HAWjTTf3QWeND6f7KY3",oauth_token="1510744291529867268-eCCNqHu1ForhIMscIdcQoopSc3Bc0W",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1649154458",oauth_nonce="uCRy17CgFsA",oauth_version="1.0",oauth_signature="iPfqIKP%2FUoJskuRQHRAsvdzW%2FFM%3D"',
  'Content-Type': 'application/json',
  'Cookie': 'guest_id=v1%3A164898541786063391; guest_id_ads=v1%3A164898541786063391; guest_id_marketing=v1%3A164898541786063391; personalization_id="v1_o5S6QbN0L1U1c9hLRaL7VQ=="'
}

# PAYLOAD
_payload = {}


#######################################
# Classes 
#######################################
# Get Tweet Instance
get = my_Twitter(_tweets_endpoint,_get_header_authorization,_payload)

#Get 10 Tweets Instance 
get_user = my_Twitter(_users_endpoint, _get_header_authorization, _payload)

#Get User ID
get_user_id = my_Twitter(_id_by_username_endpoint, _get_header_authorization, _payload )

#Post Tweet Instance
post = my_Twitter(_tweets_endpoint, _dummy_post_header_authorization,_payload)



################### PRINTING ################

def get_users_last_10():
    add_user_id = input("What is your user id: ")
    saved_user_id = 1306213626584485888
    print(get_user.get_10_tweets(add_user_id).text)

def user_id():
    username = input("Whats the username you want to get an ID for: ")
    print("User ID is:")
    print(get_user_id._get_user_id(username).text)

def post_to_twitter():
    tweet = input("What do you want to say: ")
    print(post.post_tweet(tweet).text)


# Terminal Menu 
menu_options = {
    1: 'Post To Twitter',
    2: 'Get User ID',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           post_to_twitter()
        elif option == 2:
            user_id()
        elif option == 3:
            print('Thank you for using RTP')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
    

print_menu()

