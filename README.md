
# My Sample DAGs on Apache Airflow

This project contains a collection of sample Directed Acyclic Graphs (DAGs) designed to demonstrate how to orchestrate complex workflows using Apache Airflow. These DAGs serve as examples for scheduling and automating tasks such as data processing, ETL pipelines, and other automated workflows.

The project is intended for data engineers, developers, and anyone interested in learning or experimenting with Apache Airflow to manage and automate their workflows in a reliable and scalable way.






## Acknowledgements

I appreciate the guidance of my teammate, Mostafa at SIC.


## Authors

- [@MohammadHeydari](https://github.com/mohammadheydari)


## 🚀 About Me
I'm a Senior Big Data Engineer at Sadad Informatic Corporation.





## Prerequisites

Before using these DAGs, you need to install Apache Airflow. You can follow the official installation guide from Apache Airflow's documentation or use the following command to install it via pip:

``` pip install apache-airflow ```
## Usage
1. Once Airflow is installed, clone this repository to your local machine:

```git clone https://github.com/your-username/Airflow.git```

2. Copy the DAG files from the repository into your Airflow DAGs folder. By default, the DAGs folder is located at ~/airflow/dags/:

```cp -r your-repo-name/dags/* ~/airflow/dags/```

3. Start the Airflow webserver and scheduler:

```airflow webserver --port 8080```

``` airflow scheduler```

4. Open http://localhost:8080 in your browser, and you should be able to see and trigger the DAGs in the Airflow UI.

## Note
This project is designed for data engineers, developers, and anyone interested in learning or experimenting with Apache Airflow to manage and automate their workflows in a reliable and scalable way.





