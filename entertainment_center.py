import media
import fresh_tomatoes


""" Below are the instances of the Movie calss in the media.py file"""
toy_story = media.Movie("Toy Story", "A story of a boy and his toys", "http://www.impawards.com/1995/posters/toy_story_ver1.jpg", # NOQA
 "https://www.youtube.com/watch?v=KYz2wyBy3kc")

small_soldiers = media.Movie("Small Soldiers", "A story of toys coming to life"
	, "http://www.gstatic.com/tv/thumb/movieposters/21432/p21432_p_v8_ad.jpg", 
	"https://www.youtube.com/watch?v=YwIt5wagRsg")

jungle_book = media.Movie("The Jungle Book", "A story of a human brought up in \
	jungle with Animals", "http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh", # NOQA
	 "https://www.youtube.com/watch?v=5mkm22yO-bs")
Kungfu_panda = media.Movie("Kungfu Panda", "A story of a Panda who masters mart\
	ial arts", "http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",  # NOQA
	 "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

ice_age = media.Movie("The Ice Age", "A sotry pertians to the perios of Ice Age\
	", "http://www.gstatic.com/tv/thumb/movieposters/29626/p29626_p_v8_ae.jpg",
	 "https://www.youtube.com/watch?v=cMfeWyVBidk")

inside_out = media.Movie("Inside Out", "A story of brain", "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE", # NOQA
	"https://www.youtube.com/watch?v=yRUAzGQ3nSY")


"""Below is the list of movie instances"""
movies = [toy_story, small_soldiers, jungle_book, Kungfu_panda, ice_age, inside_out]

fresh_tomatoes.open_movies_page(movies)
