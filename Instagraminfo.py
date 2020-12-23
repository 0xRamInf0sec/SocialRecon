from instagramy import InstagramUser
R = '\033[31m' 
G = '\033[32m'
C = '\033[36m'
W = '\033[0m' 

def instainfo():
    username=input("Username >> ")
    user=InstagramUser(username)
    print("-"*50)
    print(" "*15,"User name : "+username)
    print("-"*50)
    print("Full name >> ",user.fullname)
    print(' ')
    print("Biography >> ",user.biography)
    print(' ')    
    verify=user.is_verified
    if(verify == False):
        print("Verified status >> Not Verified")
        print(' ')
    else:
        print("Verified status >> Verified")
        print(' ')
    account=user.is_private
    if(account == False):
        print("Account status >> Public account")
        print(' ')
    else:
        print("Account status >> Private account")
        print(' ')
    print("URL >> ",user.website)
    print(' ')
    userphoto=user.profile_picture_url
    print("Profile Picture url >> ",userphoto)
    print('')
    print("Followers >> ",user.number_of_followers)
    print('')
    print('Following >> ',user.number_of_followings)
    print('')
    print('Posts posted >> ',user.number_of_posts)
    print('')
    
    print(G+'Completed....')
    print('')
   
if __name__=="__main__":
    instainfo()