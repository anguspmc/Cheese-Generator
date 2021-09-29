#I guess we'll start with the part that downloads // https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally



def image_get(image_url, filename):

    extention = image_url.split(".")[-1]
    #I apologise for how cursed this next line is
    filename = filename + '.' + extention
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')



def batch_image(term, amount):
    for n in range(amount):
        image_get(h, f"{term}-{amount}")

#use duck duck go api