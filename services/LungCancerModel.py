from inference_sdk import InferenceHTTPClient


class LungCancerClassifier:
    def __init__(self):
        self.CLIENT = InferenceHTTPClient(api_url="https://serverless.roboflow.com", api_key="pm1CbipadMOQEHOLmuWZ")
        self.MODEL_ID = "lung-cancer-dataset/1"

    def classify_image(self, image_url):
        return self.CLIENT.infer(image_url, model_id=self.MODEL_ID)
