""""""
import pandas as pd


#Write a program that will load the “football.csv” dataset into a dataframe called “foot_ball”. (5)
data = pd.read_csv("C:/Users/Admin/Favorites/Documents/TECHNICAL PROGRAMMING II/dataset - 2020-09-24.csv")

#3.2 inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a single python statement. (2)
print (data.head(-7))

#3.3 Write python statements to:
#3.3.1 Access and display the "Nationality" and "Club" columns for the first all players. (2)
print (data[data['Club']] [['Nationality']])

#3.3.2 Access and display the data for the tenth player in the dataset using row index. (2)
print (data.head(10))

#3.3.3 Access and display the "Goals" and "Appearances" for players with index positions 100 to 110. (2)
print (data[data['Goals']>100 -110] [['Appearances']])


#3.3.4 Add a new column named "Goals per Appearance" that is calculated by dividing "Goals" by "Appearances"; and display the first 5 rows of the updated dataset. (3)
#3.3.5 Select and display a subset of the dataframe containing only the players from "Arsenal"club. (2)
#3.3.6 Perform a filtering operation to display players who have scored more than 5. (3)
#3.4 Write a command to upgrade the pandas module so that it downloads new dependencies if needed. (2)
#3.5 Push your entire git “tp2_test1” project into the cloud repository that you created on question 1.5 and confirm that I am added as a collaborator to your project."""