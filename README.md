# ares
* The framework used here is Flask.
* For the sake of implementing the backend logic first, I have stored the files in a dir inside the app only. Moving forward that can be replaced by an S3 storage or something similar for storing the CSV filers
* The decorator methods in the run.py calls the resolvers. And the resolvers eventually refer to the data_layer methods to resolve the requests.
* The code is incomplete. Business logic is partially done and front-end, file-storing etc not done.
