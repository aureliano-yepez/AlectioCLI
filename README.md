# AlectioCLI

The Alectio client library provides an alternative to our platform website. A user is able to view experiments, projects, and other resources associated with an Alectio account. In addition, a user is able to create resources (projects + expermients), and is able to run an experiment from the command line to trigger and sdk experiment on premise.

For context, a project is a model plus dataset pair, and every project can have many active learning experiments. 


# Install Client Library 

```python
pip3 install alectio
```


## Initialize the client
```python
from alectio.client import AlectioClient
client = AlectioClient()
```

## Projects
```python
project = client.project("project_id") # grab a single project 
for experiment in project.experiments(): # grab all the project's experiemnts 
  print(experiment)
```

```python
projects = client.projects() # grab all the projects that belong to a user 
for project in projects:
    print(project)
```

## Experiments
```python
experiments = client.experiments("project_id") # grab all the experiments that belong to a project
```

```python
experiment = client.experiment("experiment_id") # grab a single experiment
```

### Running an Experiment

(TODO: provide more context, and add docs) <br>

Before running an experiment, make sure to have uploaded a query strategy or list of query strategies.
Either chose your query strategy on the Alectio Platform, or upload a YAML resource.

Example Random YAML:

```yaml
resource: Strategy
type: "regular_al"
mode: "simple"
query_strategy:
  random: 
    n_rec: 1000
    type: None 
```
Example Confidence YAML:
```yaml
resource: Strategy
type: "regular_al"
mode: "simple"
query_strategy:
  confidence:
    type: lowest
    n_rec: 100
```

```python
experiment.upload_query_strategy("path_to_yaml_file")
```


```python
experiment.start() # run an experiment 
```

# End to End Example
Before running an example, set up your SDK for your training, testing, and infering process. 
```python

 # start alectio client
 client = AlectioClient()
 
 # creating project
 print("creating alectio project.")
 project = client.create_project('./examples/project.yml')
 project_id = project.id
 
 # upload class labels file
 print("uploading class labels to project.")
 client.upload_class_labels("./examples/mnist_labels.json", project_id)
 
 os.environ['ALECTIO_PROJECT_ID'] = project_id
 
 # create experiment + pass in env variable from the created project
 print("creating alectio experiment.")
 experiment = client.create_experiment("./examples/experiment.yml")
 experiment_id = experiment.id
 
 print("uploading sample querying strategy.")
 experiment.upload_query_strategy("./examples/simple_confidence_strat.yaml")
 
 # start the experiment.
 experiment.start()
```

### Sample Class Labels
```json 
{
        "0": "airplane",
        "1": "cat",
        "2": "dog",
        "3": "truck",
        "4": "frog",
        "5": "automobile",
        "6": "horse",
        "7": "ship",
        "8": "bird",
        "9": "deer"
}
```
