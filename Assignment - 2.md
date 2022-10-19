# Assignment - 1

## Demonstration of some of the most commonly Docker commands.

### •	docker –version
This command returns the version of the Docker which is installed.

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-1.jpg)

### •	docker pull <image name>
This command is used to pull particular image which is mentioned from the Docker hub.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-2.jpg)

### •	docker images
To list all the Docker images that we have in our local system.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-3.jpg)

### •	docker –help
This command will returns a list of commands available in Docker along with the possible flags (options).
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-4.jpg)
  
### •	docker run
This command executes a Docker image on your local repo and creates a running container out of it.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-5.jpg)
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-6.jpg)

### •	docker ps
This command lists all the running containers in the host.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-7.jpg)

### • docker ps –a
This command lists both the running and the shut downed containers in the host.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-8.jpg)
  
### •	docker stop <container-id>
This command shut down the container whose container-id is specified in the arguments.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-10.jpg)

### •	docker kill <container-id>
This command kills the container by stopping its execution immediately.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-11.jpg)
  
### •	docker rm <container-id>
This command removes the container whose container-id is specified in arguments.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-12.jpg)
  
### •	docker rmi <image-name>
This command removes the image whose name is specified in arguments.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-13.jpg)
  
### •	docker logs <container-id>
This will returns the logs of the container whose container-id is specified in arguments.
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-14.jpg)

### •	docker start <container-id>
This command is used to run the container whose container-id is specified in the arguments.

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-15.jpg)

### •	docker build
This command is used to compile Dockerfile, for building custom docker images based on the dockerfile. 

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-16.jpg)

### •	docker push
This command is used to push the specified docker image to the docker hub.

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-17.jpg)
  
# Assignment - 2
  
## Hello World Docker Image Run Hello World Docker Image Locally.
  
### •	docker pull hello-world
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-18.jpg)
  
### •	docker run hello-world
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-19.jpg)
  
# Assignment - 3

## Create a hello world fastapi application. Create a Dockerfile for your fastapi hello world application. Build Docker image using Docker file. Run docker image build in previous step. Push your Docker image to Docker Hub.

### •	Creating fastapi application and Dockerfile
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-20.jpg)
  
### •	Build Docker image using Docker file 

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-21.jpg)
  
### •	Run the docker image
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-22.jpg)
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-23.jpg)
  
### •	Push Docker image to Docker Hub

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-24.jpg)
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-25.jpg)
  
# Assignment - 4
  
### Automate the bellow tasks
### •	Build docker image, and
### •	Push docker image to the docker hub.
### I have automate the above mentioned tasks using github actions.
  
### Github
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-26.jpg)
  
### Main.yaml

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-27.jpg)

### GitHub Actions
  
![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-28.jpg)
  
### Docker Repository

![download](https://github.com/AbhiGowdaIndia/Images/blob/main/image-29.jpg)  





