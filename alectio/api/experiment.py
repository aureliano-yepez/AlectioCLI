
from gql import gql

from alectio.api.base_attribute import BaseAttribute
from alectio.tools.utils import extract_id
from alectio.tools.mutations import START_EXPERIMENT_MUTATION


class Experiment(BaseAttribute):

    def __init__(self, client, attr, user_id, id):
        self._client = client
        self._attr = attr # experiment attributes
        self._user_id = user_id
        self._id = id
        self._project_id = ""
        super().__init__(self._attr, self._id)
        self.set_project_id()
        

    def metrics(self):
        """
        return the metrics for an experiment
        """
        return 

    # TODO: aureliano.
    def download_experiment_metrics(self):
        """
        download metrics for this experiment
        """
        return 

    def start(self, strategies=None):
        """
        start an experiment from the sdk
        :params: strategies - yaml file containing the strategies the user intends to use 
        for the experimennt.
        """
        # parse yaml 
        print("starting an experiment")
        query = gql(START_EXPERIMENT_MUTATION)
        params = {
            "userId": self._user_id,
            "projectId": self._project_id,
            "experimentId": self._id
        }
        # make sure the backend airlfow gets triggered 
        print(self._client.execute(query, params))

        # just pass in user_id + project_id + experiment_id
        return 

    def set_project_id(self):
        """
        return the project associated with the experiment id
        depending if the experiment comes from the get_collection query 
        or a get_single query the experiment id can be fromn the 
        sort key or primary key 
        """
        pk = extract_id(self._attr['pk'])
        sk = extract_id(self._attr['sk'])
        self._project_id = pk 
        if pk == self._id:
            self._project_id = sk
        return


    def __repr__(self):
        return "<Experiment {}>".format(self._id)


 

  

