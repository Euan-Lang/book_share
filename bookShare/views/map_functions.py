import requests
import urllib.parse
from bookShare.models import Book, UserProfile,User

#use this function to get the context dict
def getCoordsContextDict(book_id):
    userPostcode = getPostcode(book_id)
    response = getCoordsRequest(userPostcode)
    context = formatContextDict(response)
    return context


def getPostcode(book_id):


    #gets the postcode of the user from the book_id
    bookObject = Book.objects.get(book_id = book_id)
    userProfile = bookObject.user_profile
    userPostcode = userProfile.post_code
    return userPostcode


def formatContextDict(response):
    context = {}
    context["latitude"] = float(response["data"]["latitude"])
    context["longitude"] = float(response["data"]["longitude"])

    # creates a semi random number to displace the coordinates by but still keeping
    #the point within the radius
    context["latitude"] = context["latitude"] + context["longitude"] * 0.0002
    context["longitude"] = context["longitude"] + context["latitude"] * 0.0002


    centreDiff = (context["latitude"] - float(response["data"]["latitude"])) + (
                context["longitude"] - float(response["data"]["longitude"]))


    context["centreLat"] = float(response["data"]["latitude"]) + centreDiff / 2
    context["centreLng"] = float(response["data"]["longitude"]) - centreDiff / 2

    return context

def getCoordsRequest(userPostcode):
    url = urllib.parse.quote("api.getthedata.com/postcode/" + userPostcode)
    url = "https://" + url
    print(url)
    response = requests.get(url)
    response = response.json()
    return response

