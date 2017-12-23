# -*- coding=UTF-8 -*-
import media
import fresh_tomatoes

Bigfish = media.Movie(u"大鱼海棠", "a story belong to chinese",
                      "https://upload.wikimedia.org/wikipedia/zh/a/ae/Big_Fish_%26_Begonia_Ost_Cover.jpg",
                      "https://youtu.be/bH37VLQqVvo")
Cars = media.Movie("Cars",
                   "Cars would be the final film worked on by Joe Ranft who died in a car accident a year before the film's release, aged 45.",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg", "https://youtu.be/tpKSAQvCP2Y")
Flipped = media.Movie("Flipped", "The Story of first love",
                      "https://upload.wikimedia.org/wikipedia/en/3/3a/Flipped_poster.jpg",
                      "https://youtu.be/q40GxY5n2Dg")
Perfume = media.Movie("Perfume", "The Story of a Murderer",
                      "https://upload.wikimedia.org/wikipedia/en/6/69/Perfume_poster.jpg",
                      "https://youtu.be/dzy_GM2xriw")
WolfWarrior2 = media.Movie(u"战狼2",
                           "a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world. In this sequel, he finds himself in an African country protecting medical aid workers from local rebels and vicious arms dealers",
                           "https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
                           "https://youtu.be/sgJwgYIy_ug")
Chocofactory = media.Movie("Charlie and the Chocolate Factory",
                           "he storyline follows Charlie, who wins a contest and is along with four other contest winners, subsequently led by Wonka on a tour of his chocolate factory, the most magnificent in the world",
                           "https://upload.wikimedia.org/wikipedia/en/4/46/Charlie_and_the_chocolate_factory_poster2.jpg",
                           "https://youtu.be/MUn6X9lpOZE")

#add movie information into list
movie = [Bigfish, Cars, Chocofactory, Flipped, Perfume, WolfWarrior2]

# create a new movies page and open it
fresh_tomatoes.open_movies_page(movie)
