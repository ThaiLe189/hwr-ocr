echo 'build image on local'
docker build -t hidecv:v1 .
echo 'add tag'
docker tag hidecv:v1 gcr.io/ce-cbl-devall/hidecv:v1
echo 'push image on GCP'
docker push gcr.io/ce-cbl-devall/hidecv:v1