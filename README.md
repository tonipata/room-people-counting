This project aims to estimate the number of occupants in a room using machine learning models and non-intrusive environmental sensors. The system is built using FastAPI for the backend and leverages various machine learning algorithms for accurate occupancy estimation.

Requirements
To get started with the project, follow the steps below.
Set up the virtual environment
Create a virtual environment to manage project dependencies. You can create one using the following command: python -m venv <your-env-name>
This will create a virtual environment in a directory named <your-env-name>.

Install the dependencies
Once the virtual environment is set up, activate it (see the instructions for your operating system below) and install the required dependencies by running the following command:
pip install -r requirements.txt

Test the machine learning model
The machine learning model can be tested by making a POST request to the designated endpoint. The backend is implemented using FastAPI, and the endpoint allows you to send sensor data to get occupancy estimates.

To test the model:
Start the FastAPI server by running the following command:
uvicorn main:app
Once the server is running, you can make a POST request to the appropriate endpoint, passing the sensor data in the request body. You can use tools like Postman or curl to send the request.
The server will process the data and return the estimated number of occupants.
