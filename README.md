<h1>Grazioso Salvare Interactive Dashboard</h1>

<img src="https://i.imgur.com/2C4Rh7D.png" alt="Example Image" width="3000"/>


   ## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [FAQ](#faq)

## <a name="introduction"></a>Introduction

This project was created by Cameron Lee for CS-340 Client Server/Development at Southern New Hampshire University. The goal is to provide an interactive Jupyter Dashboard displaying information about dogs in a database for an international rescue-animal training company named Grazioso Salvare.

The data table includes filters for breed, age, and preferred sex to identify dogs suitable for various rescue situations, such as Water Rescue, Mountain/Wilderness Rescue, and Disaster Relief. Below is an example of the table being filtered for Mountain Rescue.
<img src="https://i.imgur.com/FY24YDU.png" alt="Example Image" width="3000"/>

Additionally, the dashboard features a reset option to clear filters. Below the data table, you'll find a real-time updating pie chart and map. The map displays the distribution of filtered dogs worldwide, pinpointing their locations and names.
<img src="https://i.imgur.com/Qf5Qe2o.png" alt="Example Image" width="3000"/>


## <a name="requirements"></a>Requirements
- Jupyter Notebook - https://jupyter.org/install
- MongoDB - https://www.mongodb.com/docs/manual/installation/
- The Project Two Dashboard Jupyter file

## <a name="installation"></a>Installation
- Download and install Jupyter Notebook and MongoDB.
- Upload the contents of the ProjectTwoDashboard.zip file into Jupyter.
- Run the notebook AFTER starting MongoDB in your command terminal.



## <a name="faq"></a>FAQ
### Why was MongoDB used as the model component of the development?

MongoDB is a simple yet effective database tool to allow one collection of information to hold and provide data easily. Its syntax is very similar to Python, which was used in the CRUD module for this project making a seamless development environment. 

### How does the Dash framework work regarding the view and controller structure?

The Dash framework was imported during the development of this project to provide a way to design and provide controls for the project. This provides a foundation for building and designing the information in a way that’s intuitive and easy to navigate. 
