# vertex-workbench-custom-images

### Steps for using a custom container image for Vertex Workbench instances

This example shows how to build a python 3.9 image from scratch, and derived from an existing container. 

### 1. Follow instructions in [CreateCustomWorkbenchContainers.ipynb](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/CreateCustomWorkbenchContainers.ipynb) to create a custom container image and save it in `Artifact Registry`

### 2. Once the image is built, navigate to `Vertex Workbench`, select `New Notebook`, and then `Customize...`

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-1.png?raw=true)

### 3. Specify a `Notebook name` and `Region`. For `Environment`, select `Custom container` 

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-2.png?raw=true)

### 4. When asked to specify the Docker container image, hit the `SELECT` button

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-3.png?raw=true)

### 5. A window will open leading to `Container Registry` and `Artifact Registry`. Find and select your image

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-4-v2.png?raw=true)

### 6. Specify desired `Machine Configuration`


### 7. The `Networking` and `Permission` fields will likely depend on your org policies. Should be able to use the same values used for non-custom-image Notebook Instances 


### 8. Under `Security`, check `Enable terminal`. Values for the other options may depend on your org policies 

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-5.png?raw=true)


### 9. Select `Create` and wait for your intance to be provisioned
> * This should only take a few minutes. 
> * Note: if your instance continues to spin without reaching a `READY` state, this could be for several reasons (e.g., your org policies could require additional steps than those outlined above)

### 10. When the instance is ready, select `Open JupyterLab`, and open a Python 3 notebook

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-6.png?raw=true)

### 11. In the notebook cell, run the code snippet below to confirm the python version

```
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
```

![create-instance](https://github.com/tottenjordan/vertex-workbench-custom-images/blob/main/docs/custom-image-7.png?raw=true)

