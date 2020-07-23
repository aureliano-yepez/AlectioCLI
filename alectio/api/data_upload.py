"""
classes related to data upload.
uploading is used to keep 
"""
from alectio.tools.mutations import UPLOAD_PARTNER_IMAGE_MUTATION


class BaseDataUpload():
    def __init__(self, client):
        self.client = client 
        self.labeling_partners = ["daivergant", "seekncheck"]

    def labeling_partner_exists(self, partner):
        """
        check if the labeling partner exists.
        :params: partner
        """
        if not partner in self.labeling_partners:
            raise "labeling partner not found"

class NumericalDataUpload(BaseDataUpload):
    """
    upload numerical data
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, numerical_file, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload numerical data.
        return 


class ImageDataUpload(BaseDataUpload):
    """
    upload image data 
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, image_path_list, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload all the images asynchronously ... 
        # TODO: make this a single request 
        for image_path in image_path_list:
            variables: {
                "file": image_path
            }
            self.client.execute(UPLOAD_PARTNER_IMAGE_MUTATION, variables=variables)
            pass

        return None

class TextDataUpload(BaseDataUpload):
    """
    upload text data 
    """
    def __init__(self, client):
        self.client = client 

    def upload_partner(self, text_file, partner, problem, meta={}):
        super().labeling_partner_exists(partner)
        # upload text data. 

        # variables: {
        #     file: None # path to the image
        # }
        
        return None 


# curl http://localhost:5005/graphql \
#   -F operations='{"query": "mutation ($file: Upload!) { uploadMutation(file: $file) { ok }}", "variables": { "file": null }}' \
#   -F map='{ "0": ["variables.file"]}' \
#   -F 0=@/Users/ayepez/Desktop/docker.png
