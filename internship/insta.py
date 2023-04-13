#Getting duplicate  data from  instagram -->instaloader

#from command prompt we can give directly
#instaloader<profile_name>
import instaloader
mod = instaloader.Instaloader()
print(mod)
#based on above project we work on different usecases
profile_name = input("Enter the Profile Name")
print(profile_name)
#mod.download_profile(profile_name)
#starts giving all posts
mod.download_profile(profile_name,profile_pic_only=True)
