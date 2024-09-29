# End_To_End_DS-Project


import dagshub
dagshub.init(repo_owner='Rizwansaifi571', repo_name='End_To_End_DS-Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)