<h1>Grazioso Salvare Interactive Dashboard</h1>

<img src="https://i.imgur.com/2C4Rh7D.png" alt="Example Image" width="3000"/>


   ## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [The Code](#code)
- [FAQ](#faq)

## <a name="introduction"></a>Introduction

This project was created by Cameron Lee for CS-340 Client Server/Development at Southern New Hampshire University. The goal is to provide an interactive Jupyter Dashboard displaying information about dogs in a database for an international rescue-animal training company named Grazioso Salvare.

The data table includes filters for breed, age, and preferred sex to identify dogs suitable for various rescue situations, such as Water Rescue, Mountain/Wilderness Rescue, and Disaster Relief. Below is an example of the table being filtered for Mountain Rescue.
<img src="https://i.imgur.com/FY24YDU.png" alt="Example Image" width="3000"/>

Additionally, the dashboard features a reset option to clear filters. Below the data table, you'll find a real-time updating pie chart and map. The map displays the distribution of filtered dogs worldwide, pinpointing their locations and names.
<img src="https://i.imgur.com/Qf5Qe2o.png" alt="Example Image" width="3000"/>

## <a name="code"></a>The Code
<p align="center">
Jupyter Dashboard
</p>
<img src="https://i.imgur.com/29yBCAv.png" alt="Example Image" width="3000"/>

The script starts by importing necessary libraries, including Dash components, Plotly, Pandas, Matplotlib, and modules related to MongoDB interaction. It sets up a connection to a MongoDB database using credentials and animal_shelter.py. It reads data from the database into a Pandas DataFrame. The layout is created using Dash HTML components and includes a title, a radio button for filtering animal types, a DataTable for displaying data, and two visualization components: a pie chart and a map. The script defines callback functions that handle interactions between different components. These interactions include updating the displayed data based on the selected filter, highlighting selected rows in the DataTable, updating styles, and generating visualizations based on the selected data. The radio button allows users to filter the displayed data based on animal rescue types such as water rescue, mountain rescue, disaster rescue, or to reset and show all animals. Selected rows in the DataTable are highlighted with a background color to provide a visual indication. The pie chart is dynamically updated based on the selected data in the DataTable. The map component displays a geochart with a marker at the location of the first animal in the selected data. It includes a tooltip and a popup with additional information about the animal.

Overall, this script integrates data retrieval from MongoDB with a web-based dashboard that allows users to interactively explore and visualize information about animals in the shelter. The dashboard provides a user-friendly interface with filters, data tables, and visualizations to enhance the understanding of the shelter data.
<p align="center">
Python
</p>
<img src="https://i.imgur.com/cwVyRzj.png" alt="Example Image" width="3000"/>
The Python code defines a class named AnimalShelter that encapsulates CRUD (Create, Read, Update, Delete) operations for a MongoDB collection representing our fictional animal shelter. The class is initialized with a MongoDB client, connecting to a database named 'AAC' (Animal Adoption Center) with authentication using a provided username and password. The code includes methods for each CRUD operation:

- Create (C): The create method adds new animal data to the MongoDB collection, checking for non-empty input data.

- Read (R): The read method retrieves data from the MongoDB collection based on a specified query and returns a cursor object, excluding the '_id' field.

- Update (U): The update method modifies existing data in the MongoDB collection based on a query and updated data. It then returns the updated data using the read method.

- Delete (D): The delete method removes data from the MongoDB collection based on a specified query and returns the remaining data using the read method.

The script uses the PyMongo library to interact with MongoDB, and the provided class offers a convenient interface for performing standard database operations on the animal shelter collection. The methods follow common CRUD principles, enabling users to manage animal data within the MongoDB database.


## <a name="requirements"></a>Requirements
- Jupyter Notebook - https://jupyter.org/install
- MongoDB - https://www.mongodb.com/docs/manual/installation/
- The Project Two Dashboard.zip file

## <a name="installation"></a>Installation
- Download and install Jupyter Notebook and MongoDB.
- Upload the contents of the ProjectTwoDashboard.zip file into Jupyter.
- Run the notebook AFTER starting MongoDB in your command terminal.



## <a name="faq"></a>FAQ
### Why was MongoDB used as the model component of the development?

MongoDB is a simple yet effective database tool to allow one collection of information to hold and provide data easily. Its syntax is very similar to Python, which was used in the CRUD module for this project making a seamless development environment. 

### How does the Dash framework work regarding the view and controller structure?

The Dash framework was imported during the development of this project to provide a way to design and provide controls for the project. This provides a foundation for building and designing the information in a way that’s intuitive and easy to navigate. 
