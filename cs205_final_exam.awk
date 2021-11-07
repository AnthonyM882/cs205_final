# TODO: Modify this file to create a shell script that is able to use awk to go through a file formatted like pokemon.dat and provides a printed report in the following format (where your script correctly calculates the values that go into the [VALUE] placeholders):
# ======= SUMMARY OF POKEMON.DAT ======
#    Total Pokemon: [VALUE]
#    Avg. HP: [VALUE]
#    Avg. Attack: [VALUE]
# ======= END SUMMARY =======

 
total_hp+=$6
total_atk+=$7

#the total_hp is all of the hp added up
#the total_atk is all of the attack added up

END {total_pokemon= NR - 1; avg_hp=total_hp/total_pokemon} 
#total_pokemon is the total of all lines, -1 is to make up the total of pokemon
#avg_hp is the avgerage of all the added up hp

END {avg_atk=total_atk/total_pokemon}
#avg_atk is the avgerage of the attack added up

END{
	{print "======= SUMMARY OF POKEMON.DAT ======"; print "   Total Pokemon: [" total_pokemon"]";print "   Avg. HP:[" avg_hp"]"; print "   Avg. Attack: ["avg_atk "]";print "======= END SUMMARY ======="}}
#the prints will print the total amount of pokemon, the avgerage hp, and avgerage attack formatted as it was instructed
	


# The "Avg." values should be calculated as mean values for the corresponding columns.
# The spacing and header formatting should match the above formatting description exactly.
# There should be a comment explaining the purpose of each line in your shell script. 
# The data file will be passed in to the script as a positional parameter and will not necessarily be called pokemon.dat. However, you can assume that any file passed to this script will be formatted exactly the way pokemon.dat is formatted.

