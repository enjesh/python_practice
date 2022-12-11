# Words requested from the user
adj1 = input("Enter an adjective: ").lower()
game = input("Enter the name of an outdoor game: ").lower()
adj2 = input("Enter another adjective: ").lower()
friend = input("Enter the name of a friend: ").capitalize()
verb = input("Enter a verb ending in 'ing': ").lower()
adj3 = input("Enter one more adjective: ").lower()

# print (adj1, game, adj2, friend, verb, adj3,)

# Story template
story = f"""It was a {adj1} summer day at the beach. 
My friends and I were in the water playing {game}. As a 
{adj2} wave came closer, my friend {friend} 
yelled, "Look! There\'s a jellyfish {verb}!" As 
we got closer, we saw that the jellyfish was indeed {verb}! {friend} ran out of the water and 
onto the sand. {friend} was afraid of {verb} jellyfish. The rest of us stayed in the water playing 
{game} because {verb} jellyfish are {adj3}."""

print(story)