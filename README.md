# Deploy A Google Cloud Function In 5 Days

Storing code relevant to PipelineToDE's [Deploy A Cloud Function In 5 Days course](https://pipe_line.ck.page/33a3ad0f36).
This repo contains a basic Python-based pipeline (and associated files), a file specifying dependencies and a CI/CD pipeline to use as an example to deploy your own Google Cloud Function on Google Cloud Platform.

The Python code is functional, but will require you to install your own API key (steps below). The main.yml file containing the CI/CD workflow is also functional. 
However, you will need to replace:

- project_id with your project_id (line 33)
- replace the project id in the event_trigger_resource variable (line 35)

![Deploy A Google Cloud Function In 5 Days (1)](https://github.com/user-attachments/assets/6728f289-c61e-477c-9875-72a1d13607aa)

# Steps To Obtain A News API Key

- Navigate to: https://newsapi.org/
- Select "Get API Key"
- Copy/Paste API key into script, configuration file or external storage
- If on a free-tier plan: Monitor usage

![Screen Shot 2024-07-31 at 4 16 54 PM](https://github.com/user-attachments/assets/7b9aae64-7305-4468-b4c2-a47969d58b41)

# Additional References

- Deploy Your Google Cloud Functions The Right Way (Medium): https://medium.com/pipeline-a-data-engineering-resource/deploy-your-google-cloud-functions-the-right-way-step-by-step-guide-f0ce22adc6c1
- A Single Screenshot Has Made Me Nearly Undefeated In GitHub Deployments: https://medium.com/pipeline-a-data-engineering-resource/a-single-screenshot-has-made-me-nearly-undefeated-in-github-deployments-e6a80e2ca17a
- Don't Just Display Your Data Science Projects, Production-ize Them: https://medium.com/pipeline-a-data-engineering-resource/dont-just-display-your-data-science-projects-production-ize-them-47537de51d80
- 5 GitHub Deployment Errors And 1 Word You Can Never Use With GCP: https://medium.com/pipeline-a-data-engineering-resource/5-github-deployment-errors-and-1-word-you-can-never-use-with-gcp-e001d1e848dc
- Overcoming The Final Hurdle Of Data Automation With Fewer Failures: https://medium.com/pipeline-a-data-engineering-resource/overcoming-the-final-hurdle-of-data-automation-with-fewer-failures-1ff060dd2b37
- An Overlooked Source Of GitHub Deployment Errors: https://medium.com/pipeline-a-data-engineering-resource/an-overlooked-source-of-github-actions-deployment-errors-d2b2ccab7ffd
- Packaging And Remote Installation With Pip, Python & Artifact Registry: https://medium.com/pipeline-a-data-engineering-resource/packaging-and-remote-installation-with-pip-python-artifact-registry-e4a715c2e3be


