# Importing the urllib module for handling HTTP requests
import urllib.request as urllib

# Defining the main function that checks connectivity to a given URL
def main(url):
    print("Checking connectivity...")
    
    # Opening the provided URL and checking its response
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully!")
    print("The response code was:", response.getcode())

# Program starts here
print("This is a site connectivity checker program")

# Taking user input for the URL
input_url = input("Input the URL of the site you want to check: ")

# Calling the main function with the user-provided URL
main(input_url)
